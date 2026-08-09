# ffplayit:

* Is just ffplay from the ffmpeg project customized for playback with a systemd unit file. 
* Designed to not interfere with another ffmpeg install.

---
for X use, you can use it from a xterminal, or edit the unit file and use it with systemd.

---



** Currently official RSEL doesn't have the vc4/v3d dri modules enabled in mesa because this is the way upstream
has it by default. fflayit  will still work anyway with some complaints and likely a few more cpu cycles.
I have a SPEC here for MESA that includes the vc4/v3d module inclusions.


For nonX console kms use make sure to add a entry for vc4
to /boot/config.txt for your rpi type:


[pi4]
#Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d-pi4
max_framebuffers=2

[pi]
#Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
max_framebuffers=2

---

for systemd kiosk use edit:

	 /usr/lib/systemd/system/ffplayit.service
