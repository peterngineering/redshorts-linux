# RedShorts / EL10

* WIP EL10 Dev Started 

**RedShorts Linux** was forked/ported from RedSleeve Linux targeting  armv7l.

My primary focus on this project is noX/console programs. 
Currently working on EGLFS noX only stuff with mythtv/ffmpeg/qtwebengine/qtbrowser.

I have a few rpi2 32bit cortex-a7 boards around and they are still useful. The deprecation of arm/aarch32 makes it
challenging on rpm systems. However, debian/raspios/alpine all keep this supported and running and I use them as reference designs
often when i hit a wall of deprecation that hasn't already been solved by RSEL.

This is from a packager and system builders perspective.
I really like alpine(super lean and mean) and its packaging is a lot like arch and some like debians apt, however. 
The rpm system has spoiled me, I have a lot of invested time/education in rpm systems and I sincerely think a RPM based system
is easier to manage and keep deps in track than alpine/debian or arch system.

What some people hate about RPMS is it's complexity however, it is this complexity and consolidation that makes 
a more consistent system IMO. Other distros are fine, I just like my building and storage in a user created repo
with binaries/patches and sources all in one convenient package. I have distro hopped and learned a lot , I started out 
on slackware but once I started building RPMS I have not seen a packing system that is better.

What I think would be a future cool project would be to retool the Alpine Linux packing system to build from scratch from a rpm/srpm
repo. I can almost hear gasping at the horror..... Seriously, I do think that would be a really nice setup with all the benefits of dep management and source management that RPM/yum/dnf brings. If you look at Oracle and all the RPM based  distros even the ones that have skewed off the RHEL path, they still enjoy a easily managed ecosystem of software. I prefer quality over quantity.

---
---

For more about arm see:
[ARM](http://en.wikipedia.org/wiki/ARM_architecture) 

**For RedShorts Linux** 9, it followed most conventions used from RedSleeve and imports it patches as required, but tries to keep the 
core repos as close to the PNAELV as possible. 

RedShorts 10 development will likely use conventions learned in version 9 and refer to other armv7 active distros upon hard stops.
  * Early on it will likely deviate from upstreams 10 srcs some until the base development rounds are done. Since Fedora stopped
     aarch32 support builds(except for a few updates) long before fc40/Stream10/EL10 hit.
      A lot will be in 'Undiscovered RPM Country!'


*  The RedShorts Linux repo here includes SPECS that are new or have changes

*  RedShorts does not have any public RPM repos at this time to host or upload everything.
*  Links for full upstream source(s) are at the bottom of this page.

*  Any tested RPMS are not yet signed.
*  You may re-use any you find and call them your own as you see fit, just share
	   back any changes please. Crediting me in any way is not necessary or required. 
		
	*  The 'Eprs' repo directory will contain custom SPECS/RPMS that are new or highly modified/custom and don't belong in the core repos.

	*  The 'devel' repo directory is the same as upstream and will also include any changed specs from the RSEL 'BuildDeps/rl9' Repo
    *  The 'raspberrypi' repo directory is the same as RSEL and contains RPI kernels and specific pkgs for RPIs

	*  Any install images provided (if any) are for testing only.

    *  Until I work out the structure, the git repo here will be messy as uploads are done manually.


---

WIP:


<code>

--

---
# Milestones: Some fun and very challenging.

Even though a lot of the hard work has seemingly already been done by redsleeve, when porting a new target you can still hit some hurdles. These are some of the big ones so far:



## Necessity of Mock: EL10 TOO?

For me, some packages will NOT build straight up with with just rpmbuild. Most of the ones that will not are due to some changes in python.
When you hit that with direct building with rpmbuild a dependency loop will occur. Here's the most often error given:

---

---
---

Finally here are some links:

**SOURCE LINKS:
  * https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi10/10/aarch64/baseos/source/SRPMS/
  * https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi10/10/aarch64/appstream/source/SRPMS/
  * https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi10/10/aarch64/codeready-builder/source/SRPMS/
  * https://dl.rockylinux.org/pub/rocky/10/BaseOS/source/tree/
  * https://dl.rockylinux.org/pub/rocky/10/AppStream/source/tree/
  * https://dl.rockylinux.org/pub/rocky/10/CRB/source/tree/
  * https://dl.rockylinux.org/pub/rocky/10/devel/source/tree/

  * https://dl.fedoraproject.org/pub/epel/10/
  * https://mirrors.rpmfusion.org/mm/publiclist/RPMFUSION%20free%20EL/10/


**Any references to 'RedShorts' imply RedShorts-Linux and is NOT related to any similar commerically naming product. RedShorts
is a hobbiest project and not commerical at this time**
