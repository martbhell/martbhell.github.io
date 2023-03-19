---
title: "Automated testing of ansible roles"
date: "2017-06-01"
categories: 
  - "it"
tags: 
  - "ansible"
  - "ci"
  - "cvmfs"
  - "docker"
  - "molecule"
  - "testing"
  - "travis"
---

## What is this?

Basic idea: whenever most things happen in your ansible repository (for example commit, pull request or release) then you want to automatically test the ansible code.

The basic tools:

- syntax-checking
- lint / codying style adherence
- actually running the code
- is it idempotent
- does the end result look like you want it to?

## How it should be done

Use something like molecule [https://github.com/metacloud/molecule](https://github.com/metacloud/molecule) which can launch your container/virtual machine, run ansible, check for lint and also run some testing framework like serverspec/testinfra.

## How I currently to do it

I use [travis](https://travis-ci.org) to test many ansible roles and playbooks. From travis you basically get an Ubuntu machine and in that you can run whatever you want.

Basic process I've used for ansible testing:

- Configure docker on the Ubuntu machine (or [LXC](https://github.com/CSCfi/ansible-role-cuda/blob/master/.travis.yml) in some roles)
- Launch a docker with the OS you want to test on (in my case mostly CentOS 7, but sometimes Debian)
- Run ansible-playbook with --syntax-check, --check and twice to check for idempotency
- Run some manual commands at the end to test whatever was configured / or at least print some config files to make sure they look OK

All of the above and more should be doable now with molecule, first and [last time I tried](https://github.com/CSCfi/ansible-role-cvmfs/tree/molecule) I couldn't get it to work but it's looking better.

## Actual commands to test

- ansible-playbook --syntax-check
- [ansible-lint](https://github.com/willthames/ansible-lint)
- ansible-playbook
- ansible-playbook
- ansible-playbook --check

### Order Matters

Do you want to run it in noop mode ( --check ) before or after the role has first run at least once to configure all the things?

## How to actually set this up

[Official travis documentation](https://docs.travis-ci.com/)

Login with your github account on travis.org (or travis.com if it's a private repo) ( and connect your github organization ).

Enable the repository, for example https://travis-ci.org/CSCfi/ansible-role-dhcp\_server

Add some files to your repo. I usually copy .travis.yml and tests/ directory from an existing repository like [ansible-role-cvmfs](https://github.com/CSCfi/ansible-role-cvmfs) .

Modify the test playbook - tests/test.yml to include the new role, maybe change some default variables and have a look in [test-in-docker-image.sh](https://github.com/CSCfi/ansible-role-cvmfs/blob/molecule/tests/test-in-docker-image.sh) script if there are anything you want to add or remove from there too.

Push to github and watch the build log :)

## Working Fighting with Travis

Fighting with docker took a lot of my time when getting this working the first time. Especially as I use ansible to configure servers that run multiple services and want to have a full systemd inside the container.

Commands to run on an Ubuntu 14.04 VM to get a kind of similar environment as in travis:

sudo apt update
sudo apt upgrade
sudo apt install build-essential libssl-dev libffi-dev python-dev git
sudo apt install docker.io cgroup-lite
/usr/share/docker.io/contrib/check-config.sh 
echo 'DOCKER\_OPTS="-H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock -s devicemapper"' | sudo tee /etc/default/docker > /dev/null
sudo cgroups-mount

And then from there run the commands you have in .travis.yml
