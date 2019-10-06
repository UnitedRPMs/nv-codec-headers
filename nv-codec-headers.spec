Name:           nv-codec-headers
Version:        9.1.23.0
Release:        7%{?dist}
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
Group:          System Environment/Libraries
URL:            https://github.com/FFmpeg/nv-codec-headers
Source0:        https://github.com/FFmpeg/nv-codec-headers/archive/n%{version}/%{name}-n%{version}.tar.gz
Patch:		libdir_fix.patch
BuildArch:      noarch
       

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.


%prep
%autosetup -n %{name}-n%{version} -p1 

%build
make PREFIX=%{_prefix} 

%install
%make_install

%files
%doc README
%{_includedir}/ffnvcodec/
%{_libdir}/pkgconfig/ffnvcodec.pc


%changelog

* Fri Oct 04 2019 David Va <davidva at tuta dot io> 9.1.23.0-7
- Updated to 9.1.23.0

* Wed Sep 25 2019 David Va <davidva at tuta dot io> 9.0.18.2-7
- Updated to 9.0.18.2-7

* Fri Mar 15 2019 David Va <davidva at tuta dot io> 9.0.18.1-2
- Updated to 9.0.18.1-2

* Fri Apr 20 2018 David Vasquez <davidva at tutanota dot com> 8.1.24.1-1.gitf21433a
- Initial build rpm
