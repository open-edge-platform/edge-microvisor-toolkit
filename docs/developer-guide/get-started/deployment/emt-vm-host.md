# Deploy Other OS as Guest Virtual Machines under EMT Host

Edge Microvisor Toolit supports SR-IOV (Single Root Input/Output Virtualization), which allows it to serve as a host OS for virtualization of other operating systems, running as a guest OS in a virtual machine.

> **NOTE:** Contact Your Intel representative for more details on required resources.

## Prerequisites

1. Prepare Ubuntu Host for creating Guest VM images, as well as Guest VM images, according to the guides below:

[Kernel and Host User Space Setup](./emt-vm-host-setup.md)

[Windows Guest VM](./emt-vm-host-win-guest.md)

[Ubuntu Guest VM](./emt-vm-host-ubuntu-guest.md)

2. Adjust EMT kernel parameters

To enable SR-IOV usage in EMT Host, you need to set the following kernel parameters:

```bash
udmabuf.list_limit=8192 i915.enable_guc=3 i915.max_vfs=7 intel_iommu=on i915.force_probe=*
sudo vim /etc/default/grub
sudo grub2-mkconfig -o /boot/grub2/grub.cfg "$@"
```

> **Note:** You can learn more about specific kernel patches related to VM hosting and
> SR-IOV implementation in the relevant [SPEC file](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/SPECS/kernel/kernel.spec)

## Hosting Guest VMs under EMT

1. Transfer the prepared Guest VM images to a bootable USB Drive.

2. Convert the qcow2 image to raw image:

   ```bash
   qemu-img convert -f qcow2 -O raw ubuntu.qcow2 ubuntu22_disk.img
   qemu-img convert -f qcow2 -O raw windows.qcow2 win11_disk.img
   ```

3. Copy the images `user-apps/win11vm/disk.img` and `user-apps/ub22vm/disk.img` respectively
   before creating the bootable USB drive. During the process of creating a bootable USB drive,
   these VM images will be copied to USB drive, for installation during provisioning.

4. Follow the deployment procedure to bring up the system with Application VM,
   refer to Get Started Guide of Edge Microvisor ToolKit Standalone Node.

5. Update the config file according to your specific use case:

   Refer to [EMT Get Started Guide](../../emt-get-started.md).

   Add the following commands to the config-file to launch the automated deployment of applications VMs:

   ```bash
   - k wait --for=condition=ready pod --all --timeout=300s
   - k create ns user-apps
   - cd /opt/user-apps/helm_charts/sidecar && k apply -f <ub22_dp1.yaml>
   - cd /opt/user-apps/helm_charts/sidecar && k apply -f <usb_b2_p2.yaml>
   - cd /opt/user-apps/helm_charts/<helm-ub22_dp1> && helm install ub22vm .
   - cd /opt/user-apps/helm_charts/<helm-win11_dp1> && helm install win11vm .
   ```

## Sidecar Configuration

1. Identification of USB port details.

   The following commands helps to identify the USB ports Bus and Port numbers to map these devices in the sidecar configuration.

   ```bash
   sudo cat /proc/bus/input/devices
   sudo lsusb
   sudo lsusb -t
   ```

2. Display Port Configuration.

   The reference display port sidecar configuration yaml files are provided in the zipped file to choose the right one for the system configuration.