Summary:	Small, safe and fast formatting library
Summary(pl.UTF-8):	Mała, bezpieczna i szybka biblioteka do formatowania
Name:		libfmt
Version:	12.1.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/fmtlib/fmt/releases
Source0:	https://github.com/fmtlib/fmt/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	92eb6f492e4838e5f024ce5207beafc7
URL:		https://github.com/fmtlib/fmt
BuildRequires:	cmake >= 3.8
BuildRequires:	libstdc++-devel >= 6:4.7
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
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for fmt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki fmt.

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
%doc ChangeLog.md LICENSE README.md
%{_libdir}/libfmt.so.*.*.*
%ghost %{_libdir}/libfmt.so.12

%files devel
%defattr(644,root,root,755)
%{_libdir}/libfmt.so
%{_includedir}/fmt
%{_libdir}/cmake/fmt
%{_pkgconfigdir}/fmt.pc
