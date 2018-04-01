Summary:	Small, safe and fast formatting library
Name:		libfmt
Version:	3.0.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://mirrors.kodi.tv/build-deps/sources/fmt-%{version}.tar.gz
# Source0-md5:	b2c97427a696182b013d2cc0a2f939fe
URL:		https://github.com/fmtlib/fmt
BuildRequires:	cmake >= 2.8.12
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern formatting library.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q -n fmt-%{version}

%build
install -d build
cd build
%cmake \
	-DFMT_CMAKE_DIR="%{_libdir}/cmake/fmt" \
	-DFMT_LIB_DIR=%{_libdir} \
	-DFMT_TEST=OFF \
	-DBUILD_SHARED_LIBS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.rst ChangeLog.rst LICENSE.rst
%attr(755,root,root) %{_libdir}/libfmt.so.*.*.*
%ghost %{_libdir}/libfmt.so.3

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/fmt
%{_includedir}/fmt/format.cc
%{_includedir}/fmt/format.h
%{_includedir}/fmt/ostream.cc
%{_includedir}/fmt/ostream.h
%{_includedir}/fmt/posix.h
%{_includedir}/fmt/time.h
%dir %{_libdir}/cmake/fmt
%{_libdir}/cmake/fmt/fmt-config-version.cmake
%{_libdir}/cmake/fmt/fmt-config.cmake
%{_libdir}/cmake/fmt/fmt-targets-pld.cmake
%{_libdir}/cmake/fmt/fmt-targets.cmake
%{_libdir}/libfmt.so
