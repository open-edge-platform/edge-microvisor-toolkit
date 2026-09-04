#!/bin/bash
#set -x

#####################################################################################


set_part_numbers() {
    ## mapped to tinker-action
    suffix=$(fix_partition_suffix)
    cryptsetup luksDump "${DEST_DISK}${suffix}2" > /dev/null 2>&1
    if [ $? -eq 0 ];
    then
	# if rootfs is encrypted then these are the partitions
	export boot_partition=1
	export rootfs_a_partition=2
	export persistent_partition=3

	export root_hashmap_a_partition=4
	export root_hashmap_b_partition=5
	export rootfs_b_partition=6
	export roothash_partition=7

	export swap_partition=8
	export tep_partition=9
	export reserved_partition=10
	export singlehdd_lvm_partition=11
    else
	export boot_partition=1
	export rootfs_a_partition=2
	export persistent_partition=3

	export rootfs_b_partition=4

	export swap_partition=5
	export tep_partition=6
	export reserved_partition=7
	export singlehdd_lvm_partition=8

    fi
}


#####################################################################################
select_partition() {

    #returns the uuid this script needs to search for to select the rootfs
    required_part=$( grep -o "boot_uuid=.* " /proc/cmdline | cut -c 11-46 )

    # blkid prints "<device>: UUID=..."; keep the last character of the device
    # name, which is the partition number
    rootfs_number=$(blkid | grep -i "$required_part" | grep -v '/dev/mapper' | sed -n 's/^[^:]*\(.\):.*/\1/p')
    if [[ "$rootfs_number" -eq "2" ]];
    then
	export rootfs_partition="rootfs_a"
	export rootfs_hash_partition="root_a_ver_hash_map"
	export roothash_filename="part_a_roothash"
	export rootfs_hash_partition_number=4
    elif [[ "$rootfs_number" -eq "6" ]];
    then
	export rootfs_partition="rootfs_b"
	export rootfs_hash_partition="root_b_ver_hash_map"
	export roothash_filename="part_b_roothash"
	export rootfs_hash_partition_number=5
    else
	export rootfs_partition=" "
	export rootfs_hash_partition=" "
	export roothash_filename=" "
	exit 1
    fi

    export rootfs_num=$rootfs_number
    
    
    
}

#####################################################################################
fix_partition_suffix() {
    part_variable=''
    ret=$(grep -i "nvme" <<< "$DEST_DISK")
    if [ $? == 0 ]
    then
        part_variable="p"
    fi

    echo $part_variable
}

#####################################################################################
get_partition_suffix() {
    part_variable=''
    ret=$(grep -i "nvme" <<< "$1")
    if [ $? == 0 ]
    then
        part_variable="p"
    fi

    echo $part_variable
}

#####################################################################################
enable_other_parts() {
    luks_key=$1
    list_block_devices=($(lsblk -dn -o NAME,TYPE | grep -iE '^(sd|nvme)[^[:space:]]*[[:space:]]+disk' | sed 's/[[:space:]].*//'))

    ## the SIZE and RM columns could also be used to skip devices with a size of
    ## 0B or removable devices (RM set to 1). See get_dest_disk().
    list_of_lvmg_part=''
    for block_dev in "${list_block_devices[@]}";
    do
	grep -i "${DEST_DISK}" <<< "/dev/${block_dev}"
	if [ $? -eq 0 ]
	then
	    continue
	fi
	
	parts=$(lsblk -ln -o NAME,TYPE "/dev/${block_dev}" | grep -v 'disk' | sed 's/[[:space:]].*//')
	for part in $parts;
	do
	    echo "check on /dev/$part"
	    cryptsetup luksDump "/dev/$part"
	    if [ $? -eq 0 ]
	    then
		# needs luks enable
		if [ ! -e "${block_dev}_crypt" ];
		then
		    echo -n $luks_key |  cryptsetup open --type luks "/dev/$part" "${block_dev}_crypt" --key-file -
		fi
	    fi
	done
    done
    
}

#####################################################################################
get_dest_disk()
{
    disk_device=""

    ## skip block devices with a size of 0B and removable devices (RM set to 1)
    list_block_devices=($(lsblk -dn -o NAME,TYPE,SIZE,RM | \
        grep -iE '^(sd|nvme)[^[:space:]]*[[:space:]]+disk[[:space:]]+[^[:space:]]+[[:space:]]+0$' | \
        grep -vE '[[:space:]]0B[[:space:]]' | sed 's/[[:space:]].*//'))
    for block_dev in "${list_block_devices[@]}";
    do
        #if there were any problems when the ubuntu was streamed.
        blkid /dev/$block_dev* | grep -i rootfs
        if [ $? -ne 0 ];
        then
           continue
        fi

        disk_device="/dev/$block_dev"
		break
    done

    if [[ -z $disk_device ]];
    then
        echo "Failed to get the disk device: Most likely no OS was installed"
        exit 0
    fi

    export DEST_DISK=$disk_device
    echo "DEST_DISK set as $DEST_DISK"
}

#####################################################################################
cleartext_dm_verity() {

    export roothash_partition=7
    export swap_partition=8

    suffix=$(fix_partition_suffix)

    # rootfs verity
    if [ ! -e /dev/mapper/rootfs_verity ];
    then
	mkdir /temp
	mount "${DEST_DISK}${suffix}${roothash_partition}" /temp
	root_hash=$(cat /temp/${roothash_filename})

	#root_num and hash partition numbers come from the function select_partition
	veritysetup open "${DEST_DISK}${suffix}${rootfs_num}" rootfs_verity  "${DEST_DISK}${suffix}${rootfs_hash_partition_number}" $root_hash
    fi

    if [ -e /temp ];
    then
	umount /temp
	rm -rf /temp
    fi

}

#####################################################################################
check_if_luks_enabled() {
    suffix=$(fix_partition_suffix)
    discard=$(cryptsetup luksDump "${DEST_DISK}${suffix}${rootfs_a_partition}")
    if [ $? -ne 0 ];
    then
	echo "Luks partition not available at ${DEST_DISK}${suffix}${rootfs_a_partition}"
	# now check if there is DM-verity alone enabled on the rootfs
	# here have to hard code the rootfs_a_hash partition because it becomes a cyclic dependency
	# it still enables dm-verity on the correct rootfs
	check=$(partx -o NAME -g "${DEST_DISK}${suffix}4" | grep -i "hashmap_a" )
	if [ $? -eq 0 ];
	then
	    #enable dm_verity for the selected rootfs
	    #un-encrypted dm-verity
	    cleartext_dm_verity
	    exit 0
	else

	    # in such a situation make rootfs part as /dev/mapper/rootfs_verity just to
	    # make it boot.
	    # Selection of the rootfs will happen based on the boot_uuid which is passed as arg
	    # if FDE is not enabled then  we just created a logical partition to continue to boot.

	    dmsetup create rootfs_verity --table \
		    "0 $(blockdev --getsize ${DEST_DISK}${suffix}${rootfs_num}) linear ${DEST_DISK}${suffix}${rootfs_num} 0"
	    exit 0
	fi
    fi
}
#####################################################################################

luks_enable()
{

    # Get rootfs
    get_dest_disk

    #set partition numbers
    set_part_numbers

    suffix=$(fix_partition_suffix)

    export TPM2TOOLS_TCTI="device:/dev/tpmrm0"

    luks_key=$(/usr/bin/tpm2-initramfs-tool unseal --pcrs 15)

    #check if there is a need to proceed with luks enable
    check_if_luks_enabled

    if [ ! -e /dev/mapper/rootfs_a ];
    then
	cryptsetup luksDump "${DEST_DISK}${suffix}${rootfs_a_partition}" > /dev/null 2>&1 && \
	    echo -n $luks_key |  cryptsetup open --type luks "${DEST_DISK}${suffix}${rootfs_a_partition}" rootfs_a --key-file -
    fi

    if [ ! -e /dev/mapper/root_a_ver_hash_map ];
    then
	cryptsetup luksDump "${DEST_DISK}${suffix}${root_hashmap_a_partition}" > /dev/null 2>&1 && \
	    echo -n $luks_key |  cryptsetup open --type luks "${DEST_DISK}${suffix}${root_hashmap_a_partition}" root_a_ver_hash_map --key-file -
    fi

    if [ ! -e /dev/mapper/ver_roothash ];
    then
	cryptsetup luksDump "${DEST_DISK}${suffix}${roothash_partition}" > /dev/null 2>&1 && \
	    echo -n $luks_key |  cryptsetup open --type luks "${DEST_DISK}${suffix}${roothash_partition}" ver_roothash --key-file -
    fi

    if [ ! -e /dev/mapper/rootfs_b ];
    then
	cryptsetup luksDump "${DEST_DISK}${suffix}${rootfs_b_partition}" > /dev/null 2>&1 && \
	    echo -n $luks_key |  cryptsetup open --type luks "${DEST_DISK}${suffix}${rootfs_b_partition}" rootfs_b --key-file -
    fi

    if [ ! -e /dev/mapper/root_b_ver_hash_map ];
    then
	cryptsetup luksDump "${DEST_DISK}${suffix}${root_hashmap_b_partition}" > /dev/null 2>&1 && \
	    echo -n $luks_key |  cryptsetup open --type luks "${DEST_DISK}${suffix}${root_hashmap_b_partition}" root_b_ver_hash_map --key-file -
    fi


    if [ -e /dev/mapper/root_b_ver_hash_map ];
    then
	mkdir /temp
	mount /dev/mapper/ver_roothash /temp
	root_hash=$(cat /temp/${roothash_filename})
    fi

    # rootfs verity
    if [ ! -e /dev/mapper/rootfs_verity ] && [ -e /dev/mapper/${rootfs_partition} ];
    then
	veritysetup open /dev/mapper/${rootfs_partition} rootfs_verity  /dev/mapper/${rootfs_hash_partition} $root_hash
    fi

    if [ -e /temp ];
    then
	umount /temp
	rm -rf /temp
    fi

    #swap
    if [ ! -e /dev/mapper/swap_crypt ];
    then
	echo -n $luks_key |  cryptsetup open --type luks "${DEST_DISK}${suffix}${swap_partition}" swap_crypt --key-file -
    fi
    
    #persistent 
    if [ ! -e /dev/mapper/edge_persistent ];
    then
	cryptsetup luksDump "${DEST_DISK}${suffix}${persistent_partition}" > /dev/null 2>&1 && \
	    echo -n $luks_key |  cryptsetup open --type luks "${DEST_DISK}${suffix}${persistent_partition}" edge_persistent --key-file -
    fi

    # Add lvm crypt
    #### single hdd lvm only if that partition is present 
    if [ -e "${DEST_DISK}${suffix}${singlehdd_lvm_partition}" ];
    then
	cryptsetup luksDump "${DEST_DISK}${suffix}${singlehdd_lvm_partition}" > /dev/null 2>&1 && \
	    echo -n $luks_key |  cryptsetup open --type luks "${DEST_DISK}${suffix}${singlehdd_lvm_partition}" lvmvg_crypt --key-file -
    fi
    
    #### lvm for all 2ndry disks
    enable_other_parts $luks_key
    
    
    udevadm trigger
}

#####################################################################################
main()
{
    select_partition
    luks_enable

}

#####################################################################################
main
