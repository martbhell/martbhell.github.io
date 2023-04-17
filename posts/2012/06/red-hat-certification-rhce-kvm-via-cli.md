---
title: Red Hat Certification - RHCE - KVM via CLI
date: 2012-06-16
category: it
tags: certification, kvm, libvirt, libvirtd, linux, qemu, red, hat, rhce, scientific, linux, studying, virtualization

In a previous [post](https://www.guldmyr.com/rhcsa-preparation/) while preparing for RHCSA I installed kvm post-installation, via the GUI.

But how to install, configure and use it only from the CLI?

## Virt-Manager

[http://virt-manager.org/page/Main\_Page](http://virt-manager.org/page/Main_Page) has some details

As a test-machine I'm using a server with Scientific Linux 6.2 (with virtualization enabled as seen by 'cat /proc/cpuinfo|grep vmx').

None of the Virtualization Groups are installed, as seen by 'yum grouplist'. While doing that you'll find four different groups. You can use

yum groupinfo "Virtualization Client"

or correspondingly to get more information about the group.

yum groupinstall Virtualization "Virtualization Tools" "Virtualization Platform" "Virtualization Client"

This installs a lot of things. Libvirt, virt-manager, qemu, gnome and python things.

lsmod|grep kvm
service libvirtd start
lsmod|grep kvm

This also sets up a bridge-interface (virbr0).

Now, how to install a machine or connect to the hypervisor?

How to get console?

ssh -XYC user@kvmserver
virt-manager

did not work.

On the **client** you could try to do:

yum groupinstall "Virtualization Client"
yum install libvirt
virt-manager

Then start virt-manager and connect to your server. However this didn't work for me either. Is virtualization needed on the client too?

Noit is not, first: check if Virtualization is enabled on the server. Look in /var/log/messages for

kernel: kvm: disabled by bios

If it says that you'll need to go into BIOS / Processor Options / and enable Virtualization.

Then you can start virt-manager, check that you can connect to the KVMserver.

Copy a .iso to /var/lib/libvirt/images on the server.

Re-connect to the kvm-server in virt-manager.

Add a new VM called **test**. Using 6.2 net-install and NAT network interface. This may take a while.

Pointing the VM to kvm-server where a httpd is running (remember firewall rules) and an SL 6.2 is stored. Installing a Basic Server.

OK, we could use virt-manager, it's quite straight-forward and doesn't require any edits of config files at all.

## Moving on to **virsh**.

To install a vm you use 'virt-install'.

You can get lots of info from 'virsh'

virsh pool-list
virsh vol-list default
virsh list
virsh list-all
virsh dumpxml test > /tmp/test.xml
cp /tmp/test.xml /tmp/new.xml

Edit new.xml

change name to new and remove line with UUID

virt-xml-validate /tmp/new.xml
virsh help create
virsh create --file /tmp/new.xml
virsh list

This creates a new VM that uses the same disk and setup. But, if you shut down this new domain, it will disappear from virsh list --all and the list. To keep it you need to define it first:

virsh define --file /tmp/new.xml
virsh start new

This can become quite a bit more complicated. You would probably want to make clones (virt-clone) or snapshots (virsh help snapshot) instead of using the same disk file.

Making your own .xml from scratch looks fairly complicated. You could use 'virt-install' however.

virt-install --help
virt-install -n awesome -r 1024 --vcpus 1 --description=AWESOME --cdrom /var/lib/libvirt/images/CentOS-6.2-x86\_64-netinstall.iso --os-type=linux --os-variant=rhel6 --disk path=/var/lib/libvirt/images/awesome,size=8 --hvm

For this the console actually works while running 'virt-install' over ssh on the kvm-server.

To make edit to a vm over ssh:

virsh edit NAMEOFVM
