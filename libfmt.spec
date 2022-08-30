Summary:	Small, safe and fast formatting library
Summary(pl.UTF-8):	Mała, bezpieczna i szybka biblioteka do formatowania
Name:		libfmt
Version:	9.1.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/fmtlib/fmt/releases
Source0:	https://github.com/fmtlib/fmt/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	21fac48cae8f3b4a5783ae06b443973a
URL:		https://github.com/fmtlib/fmt
BuildRequires:	cmake >= 3.1.0
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern formatting library.

%description -l pl.UTF-8
Nowoczesna biblioteka formatująca

%package devel
Summary:	Header files for fmt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki fmt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for fmt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki fmt.

%package static
Summary:	Static fmt library
Summary(pl.UTF-8):	Statyczna biblioteka fmt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static fmt library.

%description static -l pl.UTF-8
Statyczna biblioteka fmt.

%prep
%setup -q -n fmt-%{version}

%build
install -d build
cd build
%cmake .. \
	-DFMT_CMAKE_DIR="%{_libdir}/cmake/fmt" \
	-DFMT_LIB_DIR=%{_libdir} \
	-DFMT_TEST=OFF

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
%ghost %{_libdir}/libfmt.so.9

%files devel
%defattr(644,root,root,755)
%{_libdir}/libfmt.so
%{_includedir}/fmt
%{_libdir}/cmake/fmt
%{_pkgconfigdir}/fmt.pc
