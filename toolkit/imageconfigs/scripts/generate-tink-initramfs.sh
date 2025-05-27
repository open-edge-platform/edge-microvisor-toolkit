#!/bin/bash

# Copyright (c) Intel Corporation.
# Licensed under the MIT License.

set -e
#set -x

pprefix="Tink"

function generate_images() {
    if [[ $# -eq 2 ]]; then
        fpath=$(realpath "$1")
        if [[ $? -ne 0 || ! -f "$fpath" || ! -s "$fpath" ]]; then
            echo "Error: $fpath invalid/zero sized" | tee -a "$LOG_FILE"
            exit 255
        fi
    else
        echo "Error: Invalid param to ${FUNCNAME[0]}"
        exit 255
    fi
    local arfname="rootfs"
    cp "$1" "/tmp/$arfname.tar.gz"
    local outputdir="$2"

    tar -xvf "/tmp/$arfname.tar.gz" -C "$outputdir" --strip-components=2 --wildcards ./boot/vmlinuz-*.emt3 ./boot/initramfs-*.emt3.img
    gunzip -f "/tmp/$arfname.tar.gz"
    tar -vf "/tmp/$arfname.tar" --delete ./tmp ./boot
    gzip -f "/tmp/$arfname.tar"
    #cp "/tmp/$arfname.tar.gz" "$outputdir"

    ramfs=$(find $outputdir -type f -name initramfs*img -printf '%f\n')
    echo "pprefix: Original $ramfs $(sync;du -h $outputdir/$ramfs)"
    # unzip initramfs
    mkdir -p /tmp/initramfs
    cd /tmp/initramfs
    echo "pprefix: inside $(pwd)"
    echo "pprefix: unziping initial initramfs for repack"
    gunzip -c -k "$outputdir/$ramfs" | cpio -idmv --no-absolute-filenames
    #echo "pprefix: free space $(df -h)"

    cp "/tmp/$arfname.tar.gz" /tmp/initramfs/
    find . | cpio -o -H newc | gzip > "$outputdir/$ramfs"
    cd -

    echo "pprefix: $(sync;du -h $outputdir/$ramfs)"
    rm -rf /tmp/initramfs
    chmod 0666 $outputdir/vmlinuz-*.emt3 $outputdir/initramfs-*.emt3.img
}

# inputs
emtfile=""
odir=""

function parse_arg() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|-\?|--help)
                printf "Usage: %s [-h] <-f emt_tar_gz_file> [-o output_dir]\n" "$(basename "${BASH_SOURCE[0]}")"
                exit
                ;;

            -f)
                emtfile=$(realpath "$2")
                if [[ ! -f "$emtfile" || $(tar -tvf "$emtfile" &> /dev/null) ]]; then
                    echo "Error: $2 invalid tar.gz file"
                    return 255
                fi
                echo "Info: input file $emtfile"
                shift
                ;;

            -o)
                odir=$(realpath "$2")
                if [[ ! -d "$odir" ]]; then
                    echo "Error: $2 invalid output directory"
                    return 255
                fi
                echo "Info: output directory $odir"
                shift
                ;;

            -?*)
                echo "Error: Invalid option: $1"
                show_help
                return 255
                ;;
            *)
                echo "Error: Unknown option: $1"
                return 255
                ;;
        esac
        shift
    done
}

#-------------    main processes    -------------
trap 'echo "Error $(realpath ${BASH_SOURCE[0]}) line ${LINENO}: $BASH_COMMAND"' ERR

parse_arg "$@" || exit 255
if [[ -z "$odir" ]]; then
    odir=$(pwd)
fi
generate_images "$emtfile" "$odir" || exit 255
