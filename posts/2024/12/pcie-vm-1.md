---
title: PCI Layout inside virtual machine
date: 2024-12-29 22:57
category: it
lang: en
tags: kvm, qemu, libvirt, pcie, pci, XML, ib, infiniband, gpu, h100, virtualization
<!-- prettier-ignore -->
---

## At $Dayjob

I have managed to with PCI passthrough pass in devices(GPU and IB) into a VM.

But for some reason an all_reduce is still slow (1/10 out of 2 nodes in BM).

Layout is something like:

```text
upstream_port
^
downstream_port
^      ^      ^     ^   ^
GPU1   GPU2   GPU3  ..  GPU8
IB1    IB2    IB3   ..  IB8
```

Where the upstream & downstream ports show up as Texas Instruments PCIe switches
and are `<controllers>` in libvirt XML.

Theories / Next Steps:

- NUMA domains are not sent in properly into the VM and it doesn't know which
  cores are in which domain
- There are more ways to setup the layouts, maybe different models on the
  controllers?
- [gpu_burn](https://github.com/wilicc/gpu-burn) maybe doesn't like the above
  layout?
- Run NCCL with `TOPO_DUMP` to get the topography on a baremetal and then use
  this layout inside VM? Maybe with some small modifications?
- Read server & CPU & system board manuals to get understanding of how layout
  actually is
- Read [libvirt python](https://libvirt-python.readthedocs.io/) docs, maybe
  there are some more clues there than what already found in
  [Domain XML format](https://libvirt.org/formatdomain.html)?

### Update 2

The setup I had managed to create was one upstream and one downstream PCI device
visible in lspci per each GPU/IB card pair.

Taking a step back however with the cards passed into the VM I could only get
35Gbps between two VMs.

Theories:

- MTU? Or does infiniband figure that out based on what is set in the partition?
- Is there a better way to test this than `ib_write_bw` ?
  - Maybe some parameters to do it in parallel, does that increase bandwidth?
- ATS ON did not help.
