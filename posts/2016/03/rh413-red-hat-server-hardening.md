---
title: "RH413 - Red Hat Server Hardening"
date: "2016-03-18"
categories: 
  - "it"
tags: 
  - "redhat"
  - "rh413"
  - "security"
  - "server-hardening"
---

I'm attending this training in a week or so. This post will be updated as I go through the sections I want to check out before the training starts.

### https://www.redhat.com/en/services/training/rh413-red-hat-server-hardening

- Track security updates
    - Understand how Red Hat Enterprise Linux produces updates and how to use yum to perform queries to identify what errata are available.
- Manage software updates
    - Develop a process for applying updates to systems including verifying properties of the update.
- Create file systems
    - Allocate an advanced file system layout and use file system encryption.
- Manage file systems
    - Adjust file system properties through security related options and file system attributes.
- Manage special permissions
    - Work with set user ID (SUID), set group ID (SGID), and sticky (SVTX) permissions and locate files with these permissions enabled.
- Manage additional file access controls
    - Modify default permissions applied to files and directories; work with file access control lists.
- Monitor for file system changes
    - Configure software to monitor the files on your machine for changes.
- Manage user accounts
    - Set password-aging properties for users; audit user accounts.
- Manage pluggable authentication modules (PAMs)
    - Apply changes to PAMs to enforce different types of rules on users.
- Secure console access
    - Adjust properties for various console services to enable or disable settings based on security.
- Install central authentication
    - Install and configure a Red Hat Identity Management server and client.
- Manage central authentication
    - Configure Red Hat Identity Management rules to control both user access to client systems and additional privileges granted to users on those systems.
- Configure system logging
    - Configure remote logging to use transport layer encryption and manage additional logs generated by remote systems.
- Configure system auditing
    - Enable and configure system auditing.
- Control access to network services
    - Manage firewall rules to limit connectivity to network services.

### From the exam https://www.redhat.com/en/services/training/ex413-red-hat-certificate-expertise-server-hardening-exam

- Identify Red Hat Common Vulnerabilities and Exposures (CVEs) and Red Hat Security Advisories (RHSAs) and selectively update systems based on this information
- Verify package security and validity
- Identify and employ standards-based practices for configuring file system security, create and use encrypted file systems, tune file system features, and use specific mount options to restrict access to file system volumes
- Configure default permissions for users and use special file permissions, attributes, and access control lists (ACLs) to control access to files
- Install and use intrusion detection capabilities in Red Hat Enterprise Linux to monitor critical system files
- Manage user account security and user password security
- Manage system login security using pluggable authentication modules (PAM)
- Configure console security by disabling features that allow systems to be rebooted or powered off using bootloader passwords
- Configure system-wide acceptable use notifications
- Install, configure, and manage identity management services and configure identity management clients
- Configure remote system logging services, configure system logging, and manage system log files using mechanisms such as log rotation and compression
- Configure system auditing services and review audit reports
- Use network scanning tools to identify open network service ports and configure and troubleshoot system firewalling