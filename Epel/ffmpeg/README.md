I have all the deps for FFMPEG built for armv7hl but not yet for RSEL(armv6hl). I have included the SRPM/SPEC
here and will work on the RSEL rebuilds soon.

*In a pinch one could use the SRPM here and use fc34/35 archive repos to build a quick release.

RSEL deps rebuild/todo:
<code>
No matching package to install: 'AMF-devel'
No matching package to install: 'game-music-emu-devel'
No matching package to install: 'libmysofa-devel'
No matching package to install: 'pkgconfig(caca)'
No matching package to install: 'pkgconfig(codec2)'
No matching package to install: 'pkgconfig(dav1d)'
No matching package to install: 'pkgconfig(ffnvcodec)'
No matching package to install: 'pkgconfig(frei0r)'
No matching package to install: 'pkgconfig(libass)'
No matching package to install: 'pkgconfig(libavc1394)'
No matching package to install: 'pkgconfig(libbs2b)'
No matching package to install: 'pkgconfig(libchromaprint)'
No matching package to install: 'pkgconfig(libdc1394-2)'
No matching package to install: 'pkgconfig(libiec61883)'
No matching package to install: 'pkgconfig(libilbc)'
No matching package to install: 'pkgconfig(libmodplug)'
No matching package to install: 'pkgconfig(libopenmpt)'
No matching package to install: 'pkgconfig(librist)'
No matching package to install: 'pkgconfig(libzmq)'
No matching package to install: 'pkgconfig(lilv-0)'
No matching package to install: 'pkgconfig(lv2)'
No matching package to install: 'pkgconfig(netcdf)'
No matching package to install: 'pkgconfig(opencore-amrnb)'
No matching package to install: 'pkgconfig(rav1e)'
No matching package to install: 'pkgconfig(rubberband)'
No matching package to install: 'pkgconfig(schroedinger-1.0)'
No matching package to install: 'pkgconfig(soxr)'
No matching package to install: 'pkgconfig(srt)'
No matching package to install: 'pkgconfig(vapoursynth)'
No matching package to install: 'pkgconfig(vidstab)'
No matching package to install: 'pkgconfig(vo-amrwbenc)'
No matching package to install: 'pkgconfig(zimg)'
No matching package to install: 'pkgconfig(zvbi-0.2)'
No matching package to install: 'xvidcore-devel'
Not all dependencies satisfied
</code>
