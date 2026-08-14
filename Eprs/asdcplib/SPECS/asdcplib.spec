%global gittag rel_2_10_38

Name:           asdcplib
Version:        2.10.38
Release:        6%{?dist}%{?custom_vendor}
Summary:        AS-DCP file access libraries
License:        BSD
URL:            http://www.cinecert.com/asdcplib/

Source0:        https://github.com/cinecert/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
Source1:        %{name}.pc

ExcludeArch:    %{ix86}


BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc-c++
# https://fedoraproject.org/wiki/Licensing:FAQ#What.27s_the_deal_with_the_OpenSSL_license.3F
BuildRequires:  openssl-devel
BuildRequires:  xerces-c-devel

%description
Open source implementation of SMPTE and the MXF Interop “Sound & Picture Track
File” format. It was originally developed with support from DCI. Development
is currently supported by CineCert and other d-cinema manufacturers.

It supports reading and writing MXF files containing sound (PCM), picture (JPEG
2000 or MPEG-2) and timed-text (XML) essence. plain text and cipher text are
both supported using OpenSSL for cryptographic support.

%package        tools
Summary:        AS-DCP file access libraries tools

%description    tools
Open source implementation of SMPTE and the MXF Interop “Sound & Picture Track
File” format. It was originally developed with support from DCI. Development
is currently supported by CineCert and other d-cinema manufacturers.

It supports reading and writing MXF files containing sound (PCM), picture (JPEG
2000 or MPEG-2) and timed-text (XML) essence. plain text and cipher text are
both supported using OpenSSL for cryptographic support.

This package contains tools and testing programs for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{gittag}
sed -i -e 's/DESTINATION lib/DESTINATION %{_lib}/g' src/CMakeLists.txt

# rpmlint fixes
find . -name "*.h" -exec chmod 644 {} \;
find . -name "*.cpp" -exec chmod 644 {} \;
chmod 644 README.md
autoreconf -if

%configure
./configure --prefix=%{_prefix} --enable-as-02

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -p -D -m 644 README.md %{buildroot}%{_docdir}/%{name}
install -p -D -m 644 COPYING %{buildroot}%{_datadir}/licenses/%{name}
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
sed -i \
    -e 's|PREFIX|%{_prefix}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDEDIR|%{_includedir}/%{name}|g' \
    -e 's|VERSION|%{version}|g' \
    %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

sed -i -e 's|sys_lib_dlsearch_path_spec="/lib64 /usr/lib64 /lib /usr/lib"|sys_lib_dlsearch_path_spec="/lib /usr/lib"|' \
    configure

sed -i -e 's|openssl_ldflags="-L$openssl_prefix/lib64 -L$openssl_prefix/lib"|openssl_ldflags="-L$openssl_prefix/lib"|' \
    configure

sed -i -e 's|expat_lib_flags="-L$expat_prefix/lib64 -L$expat_prefix/lib -lexpat"|expat_lib_flags="-L$expat_prefix/lib -lexpat"|' \
    configure

find src/.libs -name '*.o' -name '*.a' -name '*.la' -name '*.lai' -delete
install -p -D -m 755 \
	src/.libs/libas02*.so \
	src/.libs/libasdcp*.so \
	src/.libs/libkumu*.so \
	%{buildroot}%{_libdir}
install -p -D -m 755 \
	src/.libs/as-02-info \
	src/.libs/as-02-unwrap \
	src/.libs/as-02-wrap \
	src/.libs/asdcp-info \
	src/.libs/asdcp-test \
	src/.libs/asdcp-unwrap \
	src/.libs/asdcp-util \
	src/.libs/asdcp-wrap \
	src/.libs/blackwave \
	src/.libs/j2c-test \
	src/.libs/klvsplit \
	src/.libs/klvwalk \
	src/.libs/kmfilegen \
	src/.libs/kmrandgen \
	src/.libs/kmuuidgen \
	src/.libs/pinkwave \
	src/.libs/wavesplit \
	%{buildroot}%{_bindir}
install -p -D -m 644 \
	src/ACES.h \
	src/AS_02.h \
	src/AS_02_ACES.h \
	src/AS_02_IAB.h \
	src/AS_02_internal.h \
	src/AS_DCP.h \
	src/AS_DCP_internal.h \
	src/KLV.h \
	src/KM_error.h \
	src/KM_fileio.h \
	src/KM_log.h \
	src/KM_memio.h \
	src/KM_mutex.h \
	src/KM_platform.h \
	src/KM_tai.h \
	src/KM_util.h \
	src/MDD.h \
	src/MXF.h \
	src/MXFTypes.h \
	src/Metadata.h \
	src/PCMParserList.h \
	src/dirent_win.h \
	%{buildroot}%{_includedir}/%{name}
#rm -fr  %{buildroot}%{_prefix}/targets

%files
%license COPYING
%doc README.md
%{_libdir}/libas02.so
%{_libdir}/libas02-2.10.38.so
%{_libdir}/libasdcp.so
%{_libdir}/libasdcp-2.10.38.so
%{_libdir}/libkumu.so
%{_libdir}/libkumu-2.10.38.so

 /usr/lib/libasdcp-2.10.38.so
%files devel
%{_includedir}/%{name}/*
%{_libdir}/libas02.so
%{_libdir}/libasdcp.so
%{_libdir}/libkumu.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/as-02-info
%{_bindir}/as-02-unwrap
%{_bindir}/as-02-wrap
%{_bindir}/asdcp-info
%{_bindir}/asdcp-test
%{_bindir}/asdcp-unwrap
%{_bindir}/asdcp-util
%{_bindir}/asdcp-wrap
%{_bindir}/blackwave
%{_bindir}/j2c-test
%{_bindir}/klvsplit
%{_bindir}/klvwalk
%{_bindir}/kmfilegen
%{_bindir}/kmrandgen
%{_bindir}/kmuuidgen
%{_bindir}/pinkwave
%{_bindir}/wavesplit

%changelog
* Thu Aug 13 2026 mockbuild - 2.10.38-6
- remove arm from Excludearch, convert to traditional tools

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.10.38-4
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Simone Caronni <negativo17@gmail.com> - 2.10.38-1
- Update to 2.10.38.
- Fix build on RHEL/CentOS 7.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.35-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.10.35-1
- Update to 2.10.35

* Sat Feb 08 2020 Simone Caronni <negativo17@gmail.com> - 2.10.34-1
- Update to 2.10.34.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Simone Caronni <negativo17@gmail.com> - 2.10.32-4
- Fix dependency issue after renaming asdcplib-libs.

* Sat Jun 08 2019 Simone Caronni <negativo17@gmail.com> - 2.10.32-3
- Review fixes.

* Sat May 25 2019 Simone Caronni <negativo17@gmail.com> - 2.10.32-2
- Fix RPATH on binaries.

* Tue Feb 26 2019 Simone Caronni <negativo17@gmail.com> - 2.10.32-1
- Update to 2.10.32.

* Fri Oct 19 2018 Simone Caronni <negativo17@gmail.com> - 2.10.31-1
- Update to 2.10.31.

* Mon Oct 01 2018 Simone Caronni <negativo17@gmail.com> - 2.9.30-1
- Update to 2.9.30.

* Mon Feb 27 2017 Simone Caronni <negativo17@gmail.com> - 2.7.19-3
- Adjust build requirements.
- Adjust Source URL.

* Wed Dec 21 2016 Simone Caronni <negativo17@gmail.com> - 2.7.19-2
- Add pkg-config file, as required by VLC.

* Wed Dec 21 2016 Simone Caronni <negativo17@gmail.com> - 2.7.19-1
- First build.
