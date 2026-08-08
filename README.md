# RedShorts / EL9

**RedShorts Linux** was forked/ported from RedSleeve Linux targeting  armv7l.
see:
[ARM](http://en.wikipedia.org/wiki/ARM_architecture) 

**RedShorts Linux** follows most conventions used from RedSleeve and imports it patches as required, but tries to keep the 
core repos as close to the PNAELV as possible. 

	*  RedShorts includes SPECS/RPMS/SRPMS and mockresults that are new or have changes. 

	*  RPMS here are not yet signed yet. You may re-use any you find and call them your own as you see fit, just share
	   back any changes please. Crediting me in any way  is not necessary or required. 
	
	*  Links for upstream source(s) that are NOT changed are at the bottom of this page.
	
	*  RedShorts does not have any public RPM repos at this time to host or upload everything.

	*  The 'Eprs' repo directory will contain custom RPMS that are new or highly modified/custom and don't belong in the core repos.

	*  The 'devel' repo directory is the same as upstream and includes many pkgs from RSELs/rl9 repo.

    *  The 'raspberrypi' repo directory is the same as RSEL and contains RPI kernels and specific pkgs for RPIS

	*  Any install images provided (if any) are for testing only.


---

WIP:

<img width="653" height="313" alt="image" src="https://github.com/user-attachments/assets/0be044e1-c650-4d6c-bc21-6dd926d8c905" />



<code>

mockbuild@armv7hnl-tinkerA17]$ rustc --print target-libdir
/usr/lib/rustlib/armv7-unknown-linux-gnueabihf/lib

[mockbuild@armv7hnl-tinkerA17]$ clang -print-effective-triple
armv7-redhat-linux-gnueabihf

/usr/lib/ld-linux-armhf.so.3 --help|tail -n5

[mockbuild@armv7hnl-tinkerA17] /usr/lib/ld-linux-armhf.so.3 --help|tail -n5
Legacy HWCAP subdirectories under library search path directories:
  v7l (AT_PLATFORM; supported, searched)
  tls (supported, searched)
  neon (supported, searched)
  vfp (supported, searched)

[mockbuild@armv7hnl-tinkerA17]$ gcc -v
Using built-in specs.
COLLECT_GCC=/usr/bin/gcc
COLLECT_LTO_WRAPPER=/usr/libexec/gcc/armv7hl-redhat-linux-gnueabi/11/lto-wrapper
Target: armv7hl-redhat-linux-gnueabi
Configured with: ../configure --enable-bootstrap --enable-host-pie --enable-host-bind-now --enable-languages=c,c++,fortran,lto --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=https://bugs.rockylinux.org/ --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only --enable-plugin --enable-initfini-array --without-isl --enable-multilib --with-linker-hash-style=gnu --enable-gnu-indirect-function --disable-sjlj-exceptions --with-tune=generic-armv7-a --with-arch=armv7-a --with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux --build=armv7hl-redhat-linux-gnueabi
Thread model: posix
Supported LTO compression algorithms: zlib zstd
gcc version 11.5.0 20240719 (Red Hat 11.5.0-14) (GCC)


[mockbuild@armv7hnl-tinkerA17]$ /opt/rh/gcc-toolset-15/root/bin/gcc -v
Using built-in specs.
COLLECT_GCC=/opt/rh/gcc-toolset-15/root/bin/gcc
COLLECT_LTO_WRAPPER=/opt/rh/gcc-toolset-15/root/usr/libexec/gcc/armv7hl-redhat-linux-gnueabi/15/lto-wrapper
Target: armv7hl-redhat-linux-gnueabi
Configured with: ../configure --enable-bootstrap --enable-languages=c,c++,fortran,lto --prefix=/opt/rh/gcc-toolset-15/root/usr --mandir=/opt/rh/gcc-toolset-15/root/usr/share/man --infodir=/opt/rh/gcc-toolset-15/root/usr/share/info --with-bugurl=https://bugs.rockylinux.org --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only --enable-libstdcxx-backtrace --with-libstdcxx-zoneinfo=/usr/share/zoneinfo --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --without-isl --enable-gnu-indirect-function --disable-sjlj-exceptions --with-tune=generic-armv7-a --with-arch=armv7-a --with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux --build=armv7hl-redhat-linux-gnueabi --enable-host-pie --enable-host-bind-now
Thread model: posix
Supported LTO compression algorithms: zlib zstd
gcc version 15.2.1 20260123 (Red Hat 15.2.1-7) (GCC)

</code>








*Most packages are built native on a Rpi4 or Tinker a-17 and or with mock.
Below is helpful info imported from RSEL, some bits may nor may not be needed for native building.


---
---





	




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
