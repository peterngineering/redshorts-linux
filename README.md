# RedShorts / EL9

**RedShorts Linux** was forked/ported from RedSleeve Linux , which itself is  a 3rd party [ARMv7](http://en.wikipedia.org/wiki/ARM_architecture) port of a Linux distribution of a Prominent North American Enterprise Linux Vendor (PNAELV). They object to being referred to by name in the context of clones and ports of their distribution, but if you are aware of [CentOS](http://en.wikipedia.org/wiki/CentOS), you can probably guess what [RedShorts](http://redshorts-linux.local) is based on. 

**RedShorts Linux** follows most conventions used from RedSleeve and imports it patches as required, but tries to keep the 
core repos as close to the PNAELV as possible. 
	* RedShorts only includes changes here and patches as needed. 
	* Links for upstream source(s) are in the spec files, see bottom of page for other SRPM urls.
	* Any install images provided (if any) are for testing only.
	* RedShorts does not have any public RPM repos at this time.




## Extra build instructions

Some packages needed some manual love and care to build, but not really a patch:

### BaseOS ###

| Package | SRPM | instruction
|---|---|---
| acpica-tools | acpica-tools-20210604-5.el9.src.rpm | must be build on a raspberry for a succesfull test. probably kernel version related 
| gmp | gmp-6.2.0-13.el9.src.rpm | must be build on a raspberry for a succesfull test. probably kernel version related 
| libkcapi | libkcapi-1.4.0-2.el9.src.rpm | must be build on a raspberry for a succesfull test. probably kernel version relatedd & build "--without clang_sa"
| libnl3 | libnl3-3.11.0-1.el9.src.rpm | '--nocheck' tests fail since glibc from 9.6
| libxcrypt | libxcrypt-4.4.18-3.el9.src.rpm | must be build on a raspberry for a succesfull test. probably kernel version related 
| nettle | nettle-3.9.1-1.el9.src.rpm | must be build on a raspberry for a succesfull test. probably kernel version related 
| openssl | openssl-3.2.2-6.el9_5.src.rpm | build with '-D "centos 1'
| python | python3.9-3.9.19-8.el9.1.redshorts.src.rpm | test_xml_etree_c breaks: '--nocheck'
*** | python | python3.9-3.9.16-1.el9.src.rpm | build with '-D "_gnu -gnueabihf"'
| strace | strace-6.12-1.el9.src.rpm | '--nocheck' tests fail since glibc from
 9.6

### AppStream ###

| Package | SRPM | instruction
|---|---|---
| awscli2 | awscli2-2.15.31-3.el9.src.rpm | must be build with '--nocheck'
| crash | crash-8.0.5-1.el9.src.rpm | build with "linux32"
| criu | criu-3.19-1.el9.src.rpm | build with "linux32"
| festival | festival-2.5.0-17.el9.src.rpm | build with "linux32"
| gcc-toolset-12-annobin | gcc-toolset-12-annobin-11.08-2.el9.src.rpm | must be build with '--nocheck'
| gnome-session | gnome-session-40.1.1-10.el9_6.src.rpm | build with '-D "centos 9"'
| grafana | grafana-10.2.6-7.el9_5.src.rpm |  must be build with '--nocheck'
| http-parser | http-parser-2.9.4-6.el9.src.rpm | must be build with '--nocheck'
| ipa | ipa-4.12.2-1.el9_5.3.src.rpm | build with `-D "eln 1"`
| isomd5sum | isomd5sum-1.2.3-14.el9.src.rpm | build with "linux32"
| java-1.8.0-openjdk | java-1.8.0-openjdk-1.8.0.432.b06-3.el9.src.rpm | build with "linux32"
| java-11-openjdk | java-11-openjdk-11.0.25.0.9-3.el9.src.rpm | build with "linux32"
| java-17-openjdk | java-17-openjdk-17.0.13.0.11-4.el9.src.rpm | build with "linux32"
| ksh | ksh-1.0.6-4.el9_5.src.rpm | build with "linux32"
| libomp | libomp-15.0.7-1.el9.redshorts.src.rpm | build with "linux32"
| nss | nss-3.101.0-10.el9_5.src.rpm | build with "linux32"
| openexr | openexr-3.1.1-2.el9_5.1.src.rpm | must be build with '--nocheck'
| openmpi | openmpi-4.1.1-7.el9.redshorts.src.rpm | build with "linux32"
| osbuild-composer | osbuild-composer-118-2.el9_5.rocky.0.6.src.rpm | must be build with '--nocheck'
| pgaudit | pgaudit-1.5.0-6.el9.src.rpm | remove '(Pre)' from macros.postgresql before build
| pg_repack | pg_repack-1.4.6-4.el9.src.rpm | remove '(Pre)' from macros.postgresql before build
| postgres-decoderbufs | postgres-decoderbufs-1.4.0-4.Final.el9.src.rpm | remove '(Pre)' from macros.postgresql before build
| python3.11-scipy | python3.11-scipy-1.10.1-2.el9.src.rpm | must be build with '--nocheck'
| python3.11 | python3.11-3.11.9-7.el9_5.1.src.rpm | build with '-D "_gnu -gnueabihf"' and '--nocheck'
| python3.11-lxml | python3.11-lxml-4.9.2-4.el9.src.rpm | build with '--nocheck'
| python3.12 | python3.12-3.12.5-2.el9_5.1.src.rpm | build with '-D "_gnu -gnueabihf"' and '--nocheck'
| python3.12-lxml | python3.12-lxml-4.9.3-2.el9.src.rpm | build with '--nocheck'
| redis | redis-6.2.7-1.el9.src.rpm | build with "linux32"
| s-nail | s-nail-14.9.22-6.el9.src.rpm | must be build with '--nocheck'
| satyr | satyr-0.38-3.el9.src.rpm | must be build with '--nocheck'
| squid | squid-5.5-14.el9_5.3.src.rpm | must be build with '--nocheck'
| tang | tang-14-2.el9.src.rpm | must be build with '--nocheck'
| tbb | tbb-2020.3-8.el9.src.rpm | build with "linux32"
| varnish | varnish-6.6.2-6.el9.src.rpm | must be build with '--nocheck'
| webkit2gtk3 | webkit2gtk3-2.46.3-1.el9_5.src.rpm | build with "linux32" and '-D "_lto_cflags %{nil}"'
| woff2 | woff2-1.0.2-15.el9.src.rpm | needs to be build with '-D "_target_platform redhat-linux-build"'


### extra ###

| Package | SRPM | instruction
|---|---|---
| elinks | elinks-0.12-0.58.pre6.el8.armv6hl.rpm | RPM from RedShorts 8.6 PowerTools


**SOURCE LINKS:
  * https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi9/9/aarch64/baseos/source/SRPMS/
  * https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi9/9/aarch64/appstream/source/SRPMS/
  * https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi9/9/aarch64/codeready-builder/source/SRPMS/
  * https://dl.rockylinux.org/pub/rocky/9/BaseOS/source/tree/
  * https://dl.rockylinux.org/pub/rocky/9/AppStream/source/tree/
  * https://dl.rockylinux.org/pub/rocky/9/CRB/source/tree/
  * https://dl.rockylinux.org/pub/rocky/9/devel/source/tree/
  * https://www.mirrorservice.org/sites/ftp.redsleeve.org/pub/el9/mirrors_redsleeve
  * https://dl.fedoraproject.org/pub/epel/9/
  * https://mirrors.rpmfusion.org/mm/publiclist/RPMFUSION%20free%20EL/9/


**Any references to 'RedShorts' imply RedShorts-Linux and is NOT related to any similar commerically naming product. RedShorts
is a hobbiest project and not commerical at this time**
