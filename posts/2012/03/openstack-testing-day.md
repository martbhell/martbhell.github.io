---
title: openstack testing day
date: 2012-03-10
category: it
tags: fedora, linux, openstack, operating, system, os, red, hat, testing, virtualization, vmware, workstation
<!-- prettier-ignore -->
---

Only one day late!

I actually started installing this on the 8th but I forgot to install it to hdd
so the 'yum update' failed and broke the machine with I/O errors :)

Installing it in a VMWare Workstation (fedora 64-bit type, 2, cores, 4G RAM, 20G
disk).

[http://fedoraproject.org/wiki/Test_Day:2012-03-08_OpenStack_Test_Day](http://fedoraproject.org/wiki/Test_Day:2012-03-08_OpenStack_Test_Day)

## Basic Setup

### 1

[http://fedoraproject.org/wiki/QA:Testcase_install_OpenStack_packages](http://fedoraproject.org/wiki/QA:Testcase_install_OpenStack_packages)
No problem.

### 2

[http://fedoraproject.org/wiki/QA:Testcase_setup_OpenStack_Nova](http://fedoraproject.org/wiki/QA:Testcase_setup_OpenStack_Nova)

Says that if you are doing this in a VM you need to "configure nova to use qemu
without KVM and hardware virtualization:". This is not true, as VMWare
Workstation 8 has virtualization pass-through.

```bash
[root@localhost mart]# vgcreate nova-volumes $(sudo losetup --show -f
/var/lib/nova/nova-volumes.img) No physical volume label read from /dev/loop0
Writing physical volume data to disk "/dev/loop0" Physical volume "/dev/loop0"
successfully created Volume group "nova-volumes" successfully created
```

openstack-nova-db-setup

Gives this error, which already is reported:

```text
Verified connectivity to MySQL. Creating 'nova' database. Asking openstack-nova
to sync the databse. 2012-03-09 07:28:26 WARNING nova.utils [-]
/usr/lib/python2.7/site-packages/nova/db/sqlalchemy/migrate_repo/versions/075_convert_bw_usage_to_store_network_id.py:49:
SADeprecationWarning: useexisting is deprecated. Use extend_existing.
useexisting=True)

2012-03-09 07:28:28 WARNING nova.utils [-]
/usr/lib/python2.7/site-packages/nova/db/sqlalchemy/migrate_repo/versions/081_drop_instance_id_bw_cache.py:40:
SADeprecationWarning: useexisting is deprecated. Use extend_existing.
useexisting=True)
```

Complete!

### 3

```bash
[root@localhost nova]# ADMIN_PASSWORD=$OS_PASSWORD
openstack-keystone-sample-data The default service password has been detected.
 Please consider setting an actual password in environment variable
SERVICE_PASSWORD
```

But after that it generates users.

### 4

No problems, should 'glance index' return anything at this stage?

### 5

No problems.

### 6 Add SSH keypair

No problems, just do exactly what the instructions say (don't try to be smart
and put them in .sh files for example :P).

### 7 Register Guest Images

At this point the wiki went down :/

```bash
[root@localhost ~]# glance add name=f16 is_public=true disk_format=qcow2
container_format=ovf
copy_from=<http://berrange.fedorapeople.org/images/2012-02-29/f16-x86_64-openstack-sda.qcow2>
Failed to add image. Got error: Unexpected response: 500 Note: Your image
metadata may still be in the registry, but the image's status will likely be
'killed'.
```

Yes, this is where it fall short. Manpage for clance doesn't even have the
'copy_from'. Maybe it could be downloaded? 'glance index' doesn't work either.

```python
[root@localhost ~]# glance index Failed to show index. Got error: Internal
Server error: Traceback (most recent call last): File
"/usr/lib/python2.7/site-packages/eventlet/wsgi.py", line 336, in
handle_one_response result = self.application(self.environ, start_response) File
"/usr/lib/python2.7/site-packages/webob/dec.py", line 147, in __call__ resp
= self.call_func(req, *args, **self.kwargs) File
"/usr/lib/python2.7/site-packages/webob/dec.py", line 210, in call_func return
self.func(req, *args, **kwargs) File
"/usr/lib/python2.7/site-packages/glance/common/wsgi.py", line 279, in __
response = req.get_response(self.application) File
"/usr/lib/python2.7/site-packages/webob/request.py", line 1086, in get_re
application, catch_exc_info=False) File
"/usr/lib/python2.7/site-packages/webob/request.py", line 1055, in call_a
app_iter = application(self.environ, start_response) File
"/usr/lib/python2.7/site-packages/keystone/middleware/auth_token.py", lin valid
= self._validate_claims(claims) File
"/usr/lib/python2.7/site-packages/keystone/middleware/auth_token.py", lin return
self._validate_claims(claims, False) File
"/usr/lib/python2.7/site-packages/keystone/middleware/auth_token.py", lin
self.admin_password) File
"/usr/lib/python2.7/site-packages/keystone/middleware/auth_token.py", lin return
json.loads(data)["access"]["token"]["id"] File
"/usr/lib64/python2.7/json/__init__.py", line 326, in loads return
_default_decoder.decode(s) File "/usr/lib64/python2.7/json/decoder.py", line
366, in decode obj, end = self.raw_decode(s, idx=_w(s, 0).end()) File
"/usr/lib64/python2.7/json/decoder.py", line 384, in raw_decode raise
ValueError("No JSON object could be decoded") ValueError: No JSON object could
be decoded
```

```bash
[root@localhost ~]# cd images/ [root@localhost images]# ls aki-tty ami-tty
ari-tty [root@localhost images]#
<http://berrange.fedorapeople.org/images/2012-02-29/f16->
x86_64-openstack-sda.qcow2^C [root@localhost images]# glance add name=aki-tty
is_public=true container_format =aki disk_format=aki < aki-tty/image
=================================================[100%] 7.79M/s, ETA 0h 0m 0s
=[ 2%] 1.25M/s, ETA 0h 0m 3s Failed to add image. Got error: You are not
authorized to complete this action. Details: 401 Unauthorized

This server could not verify that you are authorized to access the document you
requested. Either you supplied the wrong credentials (e.g., bad password), or yo
ur browser does not understand how to supply the credentials required.

Note: Your image metadata may still be in the registry, but the image's status w
=================================================[100%] 20.9M/s, ETA 0h 0m 0s
[root@localhost images]#
```

Stuck!
