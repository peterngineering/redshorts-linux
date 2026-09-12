# RedShorts Linux was forked/ported from RedSleeve Linux targeting armv7l.
*This project could not have been done so easily without the great previous works from RSEL devs. Thanks for sharing!*
---
My primary focus on this project is noX/console programs. Currently working on EGLFS noX only stuff with mythtv/ffmpeg/qtwebengine/qtbrowser and network tools.


## EL9-->EL10 Milestones, noted problems and procedural overview.
*Most all work is done from within a Redshorts EL9 chroot for easy prototyping upgrades/new pkgs. This makes it easy 
to go back to a backup chroot if dev system becomes broken.

### Compiled toolchain from e10 on el9.
gcc difficult to get at first, 
  * sysroot pkg in the way with 64bit hardcoding in spec
  * gcc jit, hard failed, removed 

### Early python package direct upgrade transition failed due to some changes in files at /usr/lib/rpm -->/usr/lib/rpm/redhat
Converted a mock chroot with new required package and started work within it for strict deps.
* el9 annobin had to be force removed before upgrade of toolchain.
* redhat-rpm-config-295 from el10 breaks compiles and needs work, use a fudged el9 version till near end of transition.
* redhat-rpm-config-295 also conflicts with a systemd-macro* pkg

 * Built and force upgraded el10 rpm ver 4.19 with so.10* objects.
  * Then manually built new bootstrap python 3.12 against that. 
  * Then built bootstrap dnf deps on that until 'finally"  getting a working chroot with updated working python/rpm/dnf system.
    *Very tedious work, many bootstrap versions created to bypass early attempt of x11/desktop creep into early builds.*


     <img width="1057" height="859" alt="armhf-el9to10-progress" src="https://github.com/user-attachments/assets/a6544c5d-c38b-43f2-8c2e-554dd334975b" />

---
<img width="1397" height="403" alt="el9to10gcc" src="https://github.com/user-attachments/assets/8e59812c-8249-46f5-a9e9-6c54ccc9a68a" />
---

<img width="1397" height="384" alt="dnfTest" src="https://github.com/user-attachments/assets/575b53c2-7c2d-4f49-b88e-e429039f6cfc" />


---
---
# *The 10 project specs were imported from 9, only as templates, they have not been updated yet. I will provide clean specs of changes soon.
---
