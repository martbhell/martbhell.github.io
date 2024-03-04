---
title: Red Hat Certification – RHCE – Network Services – e-mail
date: 2012-06-04
category: it
tags: centos, certification, dovecot, file, transfer, imap, linux, postfix, red, hat, rhce, sendmail, smtp, studying

[1st post](https://www.guldmyr.com/red-hat-certification-rhce-system-configuration-and-management-2/ "1st post") \- System Management and Configuration

[Objectives](https://www.redhat.com/training/courses/ex300/examobjective "on redhat.com")

# Network services

Network services are an important subset of the exam objectives. RHCE candidates should be capable of meeting the following objectives for each of the network services listed below:

- Install the packages needed to provide the service.
- Configure SELinux to support the service.
- Configure the service to start when the system is booted.
- Configure the service for basic operation.
- Configure host-based and user-based security for the service.

User should be able to do the following for all these services:

- [http/https](https://guldmyr.com/red-hat-certification-rhce-network-services-httpd)
- [dns](https://guldmyr.com/red-hat-certification-rhce-network-services-dns)
- [ftp](https://www.guldmyr.com/red-hat-certification-rhce-network-services-ftp)
- [nfs](https://www.guldmyr.com/red-hat-certification-rhce-network-services-nfs/)
- [smb](https://www.guldmyr.com/red-hat-certification-rhce-network-services-smb/)
- [smtp](https://www.guldmyr.com/red-hat-certification-rhce-network-services-e-mail/)
- ssh
- ntp

## SMTP

Hackmode has a [good article](http://www.hackmode.net/?page_id=80 "on hackmode.net") about setting postfix for the first time.

To test that e-mail is working you can - tada - use an e-mail client.

You have lots of details in /usr/share/doc/postfix-N ( the path should be in /etc/postfix/main.cf )

- Install the packages needed to provide the service.

- yum install postfix

- Configure SELinux to support the service

- getsebool -a|grep postfix

- Configure the service to start when the system is booted.

- chkconfig postfix on

- Configure the service for basic operation.

- set hostname to host.example.com
- /etc/postfix/main.cf and define (this assumes hostname is host.example.com):

- myhostname = host.example.com
- mydomain = example.com
- myorigin = $mydomain
- inet\_interfaces = all
- mydestination = add $mydomain to the default one
- home\_mailbox = Maildir/
- Update firewall to allow port 25 tcp
- Test with: nc localhost 25

- Configure host-based and user-based security for the service

- iptables or $mynetworks in main.cf
- user: postmap

In CLI (important to use ' and not "):

# hostname - record the output of this
postconf -e 'myhostname = output from hostname in here'
# hostname -d
postconf -e 'mydomain = output from hostname -d in here'
postconf -e 'myorigin = $mydomain'
postconf -e 'inet\_interface = all'
postconf -e 'mydestination = $myhostname, localhost, $mydomain'
postconf -e 'mynetworks = 127.0.0.0/8 \[::1\]/128, /32'
postconf -e 'relay\_domains = $mydestination'
postconf -e 'home\_mailbox = Maildir/'

To use it:

useradd -s /sbin/nologin labber
passwd labber

Edit /etc/aliases and add:

labber: labber

Then run:

newaliases
service postfix start
service postfix status
netstat -nlp|grep master

Send e-mail:

mail -s "Test e-mail here" labber@mydomain
test123
.

The . at the end is quite nice, that stops the input.

Check e-mail:

cat /home/labber/Maildir/new/\*

## Real E-mail Client

But, perhaps you want to check this out with a real e-mail client like thunderbird 10.

For this there needs to be a e-mail server that stores the e-mails on the server.

For this we can use 'dovecot'

yum install dovecot
service dovecot start

1. Update iptables to allow ports 25 and 143 (TCP)
2. Update main.cf to allow from your IP
3. Restart services
4. Add new account in thunderbird -

1. do use the IP address of your server, not the DNS
2. do not use SMTP security (or username), but use password authentication
3. do use IMAP STARTTLS security, username: labber, password auth

Thunderbird is quite nice, it will often tell you which setting is wrong.

You can use /var/log/maillog for details on the server-side (to see if you get connections at all for example).

## Deny a User

To illustrate this feature we first need to add a second user/e-mail account:

useradd -s /sbin/nologin labrat
passwd labrat
echo "labrat: labrat" >> /etc/aliases
newaliases
service postfix restart
service dovecot restart
mail -s "test" labrat@mydomain

You need to send an e-mail to the e-mail address before you can add it in Thunderbird (because the user does not have a $HOME/Maildir until you do).

After the new user has been created and added to your e-mail client do [the following](http://www.cyberciti.biz/faq/howto-blacklist-reject-sender-email-address/ "source"):

cd /etc/postfix
echo "labber@mydomain REJECT" >> sender\_access
postmap hash:sender\_access
echo "smtpd\_sender\_restrictions = check\_sender\_access hash:/etc/postfix/sender\_access" >> /etc/postfix/main.cf
service postfix restart

Try:

- to send an e-mail from and to both accounts

## Extra

- Configure a mail transfer agent (MTA) to accept inbound email from other systems.

- inet\_interfaces = all

- Configure an MTA to forward ([relay](http://www.postfix.org/postconf.5.html#relayhost "on postfix.org")) email through a smart host.

- relayhost=hostname.domain.com

If I understand this correctly to setup the above two we would need to have two servers.
