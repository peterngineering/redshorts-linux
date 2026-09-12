RedShorts Linux was forked/ported from RedSleeve Linux targeting armv7l.

My primary focus on this project is noX/console programs. Currently working on EGLFS noX only stuff with mythtv/ffmpeg/qtwebengine/qtbrowser.


EL9-->EL10 Milestons, Noted Problems and procdural Overview.

Compiled toolchain from e10 on el9.
gcc difficult to get at first, 
  * sysroot pkg in the way with 64bit hardcoding in spec
  * gcc jit, hard failed, removed 

Early python package direct upgrade transition failed due to some changes in files at /usr/lib/rpm -->/usr/lib/rpm/redhat
* Converted a mock chroot with new required package and started work within it for strict deps.
* el9 annobin had to be force removed before upgrade of toolchain.
* redhat-rpm-config-295 from el10 breaks compiles and needs work, use a fudged el9 version till near end of transition.
* redhat-rpm-config-295 also conflicts with a systemd-macro* pkg

 *In chroot, built and force upgraded el10 rpm ver 4.19 with so.10* objects.
   * Then manually built new boottrap python 3.12 against that. 
       Then built bootstrap dnf deps on that until 'finally"  getting a working chroot with updated working python/rpm/dnf system 
           -very tedious work, many bootstrap versions created to bypass early attempt of x11/desktop creep into early builds.