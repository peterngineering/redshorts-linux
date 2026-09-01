# RedShorts / EL9

**RedShorts Linux** was forked/ported from RedSleeve Linux targeting  armv7l.

My primary focus on this project is noX/console programs. 
Currently working on EGLFS noX only stuff with mythtv/ffmpeg/qtwebengine/qtbrowser.

I have a few rpi2 32bit cortx-a7 boards around and they are still useful. The deprecation of arm/aarch32 makes it
challenging on rpm systems. However, debian/raspios/alpine all keep this supported and running and I use them as reference designs
often when i a wall of deprecation that hasn't already been solved by RSEL.

This is from a packager and system builders perspective.
I really like alpine(super lean and mean) and it's packaging is a lot like arch and some like debians apt, however. 
The rpm system has spoiled me, I have a lot of invested time/education in rpm systems and I sincerely think a RPM based system
is easier to manage and keep deps in track than alpine/debian or arch system.

What some people hate about RPMS is it's complexity however, it is this complexity and consolidation that makes 
a more consistent system IMO. Other distros are fine, I just like my building and storage in a user created repo
with binaries/patches and sources all in one convenient package. I have distro hopped and learned a lot , I started out 
on slackware but once I started building RPMS I have not seen 

What I think would be a futre cool project would be to retool the Alpine Linux packing system to build from scratch from a rpm/srpm
repo. I can almost hear gasping at the horror..... Seriously, I do think that would be a really nice setup with all the benefits of dep management and source management that RPM/yum/dnf brings. If you look at Oracle and all the RPM based  distros even the ones that have skewed off the RHEL path, they still enjoy a easily managed ecosystem of software.


see:
[ARM](http://en.wikipedia.org/wiki/ARM_architecture) 

**RedShorts Linux** follows most conventions used from RedSleeve and imports it patches as required, but tries to keep the 
core repos as close to the PNAELV as possible. 

*  The RedShorts Linux repo here includes SPECS that are new or have changes
*  Most specs here have been tested to build against both RSEL(armv6) and Redshorts(armv7) using mock.
*  The logs from the last test build(armv6) is in : mockresults  

*  RedShorts does not have any public RPM repos at this time to host or upload everything.
*  Links for full upstream source(s) are at the bottom of this page.

*  Any tested RPMS are not yet signed.
*  You may re-use any you find and call them your own as you see fit, just share
	   back any changes please. Crediting me in any way is not necessary or required. 
   
		* Redshorts is testing a custom_vendor macro for all changed rpms. Changed SRPM specs
		will have %{?custom_vendor} appended after the {dist} macro in Release lines.
		This will be ignored  unless the macro is populated via cmd line for
		rpmbuild/mock etc  or set in .rpmmacros

			-D "custom_vendor .redsleeve"
		      or
			-D "custom_vendor .redshorts"

		
		
	*  The 'Eprs' repo directory will contain custom SPECS/RPMS that are new or highly modified/custom and don't belong in the core repos.

	*  The 'devel' repo directory is the same as upstream and will also include any changed specs from the RSEL 'BuildDeps/rl9' Repo
    *  The 'raspberrypi' repo directory is the same as RSEL and contains RPI kernels and specific pkgs for RPIs

	*  Any install images provided (if any) are for testing only.

    *  Until I work out the structure, the git repo here will be messy as uploads are done manually.


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
How did I get from redsleeve el9 to a Tinkerboard el9 ? Using a shortcut ofc!
Eg, with a little consideration for compatibility you can take distro X's kernel and its modules and copy those over to your Distro Y's userland. Then quickly use its kconfig and build a proper new kernel from source so you don't lose any nerd street cred.




---

---
# Milestones: Some fun and very challenging.

Even though a lot of the hard work has seemingly already been done by redsleeve, when porting a new target you can still hit some hurdles. These are some of the big ones so far:



## Necessity of Mock:

For me, some packages will NOT build straight up with with just rpmbuild. Most of the ones that will not are due to some changes in python.
When you hit that with direct building with rpmbuild a dependency loop will occur. Here's the most often error given:

<code>
Traceback (most recent call last):
  File "/usr/bin/g-ir-scanner", line 98, in <module>
    from giscanner.scannermain import scanner_main
  File "/usr/lib/gobject-introspection/giscanner/scannermain.py", line 35, in <module>
    from giscanner.ast import Include, Namespace
  File "/usr/lib/gobject-introspection/giscanner/ast.py", line 29, in <module>
    from .sourcescanner import CTYPE_TYPEDEF, CSYMBOL_TYPE_TYPEDEF
  File "/usr/lib/gobject-introspection/giscanner/sourcescanner.py", line 25, in <module>
    from .ccompiler import CCompiler
  File "/usr/lib/gobject-introspection/giscanner/ccompiler.py", line 29, in <module>
    from distutils.msvccompiler import MSVCCompiler
ModuleNotFoundError: No module named 'distutils.msvccompiler'
</code>

If you research this you will learn that python was modified in later versions and straight rpmbuild can not resolve it.
Soon as you try it in a chroot with mock it magically resolves the expectations for python and you can finally get a good build.
I'm sure this isn't the only reason you HAVE TO use mock, it's just the one I recall I have hit most often.

I have tested the very same SRMS against aarch64 and they build fine without mock. I'm still looking to see what the diff is,
it may turn out to be arm specific or it maybe be something with my toolchain/python setup. Note sure yet, it's just weird that
the very same source RPMS build without mock on aarch64 with no problem or error. I have reset my development system
at least 3 times from clean chroots to try and reduce errors being built upon, but something keeps creeping back in.




---

## Chicken or the egg, which is first?
Rust desires it be built with the target you want, armv6 --> armv7 will not work with --target=newtarget. 
I played with this a few times, I tried fedora armv7hl builds then quickly hit dependency mismatches that added to the problem. Eventually I found the best way around this was to use the redsleeve armv6 packages, then install the exact same version of armv7l rust from archives right over the top of the armv6
binaries. Then I was able to produce a proper armv7l-unknown-linux-gnueabihf rpm rust package. Of course I started with a new development environment after that. That was hard work but very gratifying afterwards. This approach is sometimes an easy shortcut way to get a bootstrapped version of a package.


---
## Webkit2GtK3/QtWebengine/Chromium 
These all are C++ template shuffling memory eating behemoths. On top of that, so complex with so many deps that bugs always seem to occur. Just when you think you have one problem worked out another pops up, it is like software development whack-a-mole. You can get to near the end and just when you think its gonna build, OOPS processes killed.....out of memory...
yet again. Then you tweak it for another run and open up a bug unrelated, the repeat. You can not have enough memory for these packages
it has to be a perfect configuration or it will NOT build and you will not know it will not build until your deep down the rabbit hole.

Dealing with these packages without a lot of patience will make you want to get a NEW HOBBY. 
If you want to discourage someone on the fence aka "run someone off from software development linux"
Just give them these packages with only Clang/LLVM and make them build them over and over after making small changes in between builds.
Then wait for it.


“The more they overthink the plumbing, the easier it is to stop up the drain.” Montgomery “Scotty” Scott 


I'm still working out some issues with the above, I will get a good build, eventually. 

*qtwebengine. 
After numerous iterations of QT versions and rebuilds I hit a wall with deprecated 32bit from upstream EL vendor.
I learned that nodejs starting at 20.x on rhels expect to be 64bit, since I'm native building, 'this is a problem for me.'
Patches from other arm distros bypass the issue up to qt 6.10.x, but I'll have to fudge in a nodejs 20 or patch and downgrade it
to get more movement on the qtwebengine.

*Webkit2Gtk3, still does not build for me on my armv7 redshorts or armv6 tooled redsleeve. Perhaps next I will
create a new fresh spin of RSEL arm and try again for this.

*Chromium, i have no motivation to work on x11 or wayland gui programs. I already built the basic XFCE/lightdm and a few gui apps
which is where I will stop at. If I need a broswer on arm, I would rather focus on a console browser such at qutebrowser. Which of course depends on a stable modern working qtwebengine!


I have hit other road bumps but they are not noteworthy as the above.


---
---
Below is helpful info imported from RSEL, some bits may nor may not be needed for native building. Some of the instructions
below imply building with a 64bit/32bit multilib OS.





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





---
---

Finally here are some links:

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
