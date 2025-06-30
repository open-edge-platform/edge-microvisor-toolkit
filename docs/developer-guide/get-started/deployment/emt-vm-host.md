# Deploying Other OS as Guest Virtual Machines under EMT Host

Edge Microvisor Toolit supports SR-IOV (Single Root Input/Output Virtualization), which allows it to serve as host OS for virtualization of other operating systems, running as Guest OS in a virtual machine.

To enable SR-IOV you need to ensure the following Kernel parameters are set:

```bash
udmabuf.list_limit=8192 i915.enable_guc=3 i915.max_vfs=7 intel_iommu=on i915.force_probe=*
sudo vim /etc/default/grub
sudo grub2-mkconfig -o /boot/grub2/grub.cfg "$@"
```

Resources required for configuring guest OS require access to intel proprietary storage location. Contact Your Intel representative to learn more and obtain required materials.