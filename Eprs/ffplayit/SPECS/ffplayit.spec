# customized ffplayit  build 
# static build without encoding support
# setup for decoding/playback
# 
# don't create debug pkgs
%global debug_package %{nil}

%define _unpackaged_files_terminate_build 0 
%define _missing_doc_files_terminate_build 0 

#only use X11,vaapi,vdpau on x86_64
%ifarch x86_64
%bcond_without X11
%bcond_without vaapi
%bcond_without vdpau
%endif

%ifarch %{arm}
%bcond_with X11
%bcond_with vaapi
%bcond_with vdpau
%endif

Name:           ffplayit
Version:        5.1.10
Release:        1%{?dist}%{?custom_vendor}
Summary:        ffplayit program 
License:        GPLv3+,GPLv2,LGPL v2.1+
URL:            https://ffmpeg.org/
Source0:        ffmpeg-%{version}.tar.xz
#https://ffmpeg.org/releases/ffmpeg-%%{version}.tar.xz.asc
Source1:	ffplayit.service

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm)
%ifarch %{arm}
BuildRequires:  pkgconfig(libv4l2)
%endif
BuildRequires:  pkgconfig(sdl2)
%if %{with X11} 
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXv-devel
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
%endif
%if %{with vaapi} 
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  libva-devel
%endif
%if %{with vdpau} 
BuildRequires:  libvdpau-devel
%endif
BuildRequires:  pkgconfig(zlib)

#BuildRequires:  vulkan-loader-devel
#BuildRequires:  glslang-devel


%description
ffplayit is actually ffplay from the FFmpeg project


%prep

%autosetup -n ffmpeg-%{version}

%build
%set_build_flags


#install to /usr/local to keep out of the way of any other ffmpeg
#
# This is not a normal configure script, don't use %%configure
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --docdir=%{_docdir}/%{name} \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --arch=%{_target_cpu} \
    --optflags="%{build_cflags}" \
    --extra-ldflags="%{build_ldflags}" \
    --enable-static \
    --disable-shared \
    --enable-pic \
    --disable-ffmpeg \
    --enable-ffplay \
    --enable-ffprobe \
    --enable-libdrm \
    --enable-opengl \
    --enable-pthreads \
%if %{with X11} 
    --enable-libxcb \
%else
    --disable-libxcb \
%endif
%if %{with vaapi}
    --enable-vaapi \
%else
    --disable-vaapi \
%endif
%if %{with vdpau}
    --enable-vdpau \
%else
    --disable-vdpau \
%endif
    --disable-encoders \
    --disable-ffnvcodec \
    --disable-amf \
    --disable-cuda-llvm \
    --disable-omx \
    --disable-openal \
    --disable-opencl \
    --disable-libopencv \
    --disable-libtwolame \
    --disable-libtheora \
    --disable-libvidstab \
    --disable-libfontconfig \
    --disable-libfreetype \
    --disable-libopenjpeg \
    --disable-libvorbis \
    --disable-nvenc \
    --disable-nvdec \
    --disable-libvpx \
    --disable-libwebp \
    --disable-libgsm \
    --disable-doc \
    --disable-htmlpages \
    --disable-manpages \
    --disable-podpages \
    --disable-txtpages \
    --disable-chromaprint \
    --disable-stripping \
    --disable-openssl \
    --disable-bzlib \
    --disable-gcrypt \
    --disable-gnutls \
    --disable-ladspa \
    --disable-libglslang \
    --disable-vulkan \
    --disable-cuda-sdk \
    --disable-libgsm \
    --disable-libjack \
    --disable-libmodplug \
    --disable-libmp3lame \
    --disable-libopenmpt \
    --disable-libpulse \
    --disable-librsvg \
    --disable-libvpx \
    --disable-libxml2 \
    --disable-libx264 \
    --disable-libx265 \
    --disable-libxvid \
    --disable-libxavs \
    --disable-libxavs2 \
    --disable-libxml2 \
    --disable-libzimg \
    --disable-libzmq \
    --disable-debug \
%ifarch x86_64
    --enable-lto \
    --disable-libv4l2 \
%endif
%ifarch armv6hl
    --cpu=armv6 \
    --enable-vfp \
    --disable-lto \
    --enable-libv4l2 \
    --enable-small \
    --disable-runtime-cpudetect \
    --disable-hardcoded-tables \
%endif
%ifarch armv7hl 
    --cpu=armv7-a \
    --enable-vfpv3 \
    --enable-thumb \
    --enable-lto \
    --enable-libv4l2 \
    --enable-small \
    --disable-runtime-cpudetect \
%endif
%ifarch armv7hnl
    --cpu=armv7-a \
    --enable-lto \
    --enable-neon \
    --enable-libv4l2 \
    --enable-small \
    --disable-runtime-cpudetect \
%endif
    || cat ffbuild/config.log

cat config.h

%make_build V=1
%make_build documentation V=1
%make_build alltools V=1

%install
%make_install V=1

#setup/install ffplayit.service
install --directory %{buildroot}%{_unitdir} 
install --preserve-timestamps --mode 0644 \
    --target %{buildroot}%{_unitdir} %{SOURCE1}

rm -rf %{buildroot}/%{_datadir}/%{name}
#don't include any headers/include files to build against this build
rm -rf %{buildroot}/%{_includedir}
#static build, don't include any pkgconfig or *.a  libs
rm -rf %{buildroot}/%{_libdir}/*.a
rm -rf %{buildroot}/%{_libdir}/pkgconfig
mv  %{buildroot}/%{_bindir}/ffplay %{buildroot}/%{_bindir}/ffplayit
mv  %{buildroot}/%{_bindir}/ffprobe %{buildroot}/%{_bindir}/ffprobeit

%files -n %{name}
%doc CREDITS README.md
%license COPYING.GPLv2 LICENSE.md
%{_bindir}/ffplayit
%{_bindir}/ffprobeit
%{_unitdir}/ffplayit.service

%changelog
* Sat Aug 08 2026 mockbuild - 5.1.10-1
- create rpm spec for ffplayit inspired by fc36/rpmfusion spec versions 
