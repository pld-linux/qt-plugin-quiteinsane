Summary:	QuiteInsane-Plugin - Qt plugin to access scanners
Summary(pl):	QuiteInsane-Plugin - wtyczka Qt umo¿liwiaj±ca dostêp do skanerów
Name:		qt-plugin-quiteinsane
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/quiteinsane/quiteinsane_plugin-%{version}.tar.gz
# Source0-md5:	f69678402148ada83f7e59938384a2c9
Patch0:		%{name}-setstyle.patch
URL:		http://quiteinsane.sourceforge.net/index.shtml
BuildRequires:	qt-devel >= 3.0
BuildRequires:	sane-backends-devel >= 1.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The intention behind the QuiteInsane-Plugin is to provide a
SANE-frontend as a plugin, which can be easily integrated in Qt based
applications. If you wonder, what "easy" means in this context, I can
assure you, that it's not much more than copying a few lines of code
and doing some small modifications. You have to know nothing about the
SANE library and it's API.

%description -l pl
Celem QuiteInsane-Plugin jest dostarczenie frontendu do SANE jako
wtyczki, któr± mo¿na ³atwo zintegrowaæ w aplikacjê opart± na Qt.
"£atwo" w tym kontek¶cie oznacza nie wiêcej ni¿ skopiowanie kilku
linii kodu i uczynienie paru ma³ych modyfikacji. Nie trzeba nic
wiedzieæ o bibliotece SANE ani jej API.

%prep
%setup -q -n quiteinsane_plugin-%{version}
%patch0 -p1

%build
qmake quiteinsaneplugin.pro -o Makefile \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
	QMAKE_RPATH=

%{__make} sub-quiteinsaneplugin \
	QTDIR=%{_prefix} \
	LFLAGS="%{rpmldflags} -shared -Wl,-soname,libquiteinsane_plugin_mt.so" \
	TARGET="libquiteinsane_plugin_mt.so"

%{__make} sub-plugintest \
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt

install quiteinsaneplugin/libquiteinsane_plugin_mt.so \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO doc/index.html
%attr(755,root,root) %{_libdir}/qt/plugins-mt/lib*.so
