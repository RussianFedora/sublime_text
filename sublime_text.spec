%global debug_package %{nil}
%global revision 3143

Name: sublime_text
Version: 3.0.%{revision}
Release: 2%{?dist}
Summary: Sublime Text 3

Source0: https://download.sublimetext.com/%{name}_3_build_%{revision}_x64.tar.bz2
Source1: https://download.sublimetext.com/%{name}_3_build_%{revision}_x32.tar.bz2
Source2: https://github.com/RussianFedora/sublime_text/raw/master/%{name}.desktop

URL: http://www.sublimetext.com/3
License: EULA

BuildRequires: desktop-file-utils
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires: hicolor-icon-theme

# Provide additional names for package manager.
Provides: sublimetext = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: sublimetext < %{?epoch:%{epoch}:}%{version}-%{release}
Provides: sublimetext3 = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: sublimetext3 < %{?epoch:%{epoch}:}%{version}-%{release}

# Conflicts with official malformed package.
Conflicts: sublime-text

%description
Sublime Text 3 for GNU/Linux is a sophisticated text editor for code, markup
and prose.

%prep
%ifarch x86_64
%setup -q -T -b 0 -n %{name}_3
%else
%setup -q -T -b 1 -n %{name}_3
%endif

%build
# Do nothing...

%install
# Creating general directories...
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}/opt/%{name}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{256x256,128x128,48x48,32x32,16x16}/apps/

# Creating ghost file for alternatives system...
touch %{buildroot}%{_bindir}/%{name}

# Installing to working directory from official package...
mv %_builddir/%{name}_3/* %{buildroot}/opt/%{name}/

# Removing build-in desktop file...
rm -f %{buildroot}/opt/%{name}/%{name}.desktop

# Installing icons...
mv %{buildroot}/opt/%{name}/Icon/256x256/sublime-text.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
mv %{buildroot}/opt/%{name}/Icon/128x128/sublime-text.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mv %{buildroot}/opt/%{name}/Icon/48x48/sublime-text.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mv %{buildroot}/opt/%{name}/Icon/32x32/sublime-text.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
mv %{buildroot}/opt/%{name}/Icon/16x16/sublime-text.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

# Removing empty directories...
rm -rf %{buildroot}/opt/%{name}/Icon

# Marking as executtable...
chmod +x %{buildroot}/opt/%{name}/%{name}

# Creating desktop icon...
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} /opt/%{name}/%{name} 10

%postun
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} /opt/%{name}/%{name}
fi

%files
/opt/%{name}
%ghost %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Oct 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3143-2
- Use alternatives to provide /usr/bin/sublime_text binary.

* Thu Sep 14 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3143-1.R
- Updated to 3.0.3143 (release).

* Sat Sep 24 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3126-1.R
- Updated to 3.0.3126.

* Thu Sep 22 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3124-1.R
- Updated to 3.0.3124.

* Wed Jul 06 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3114-2.R
- Updated desktop file. Fixed issue with Gnome 3. Updated Requires.

* Fri May 13 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 3.0.3114-1.R
- update to 3.0.3114

* Mon Feb 15 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3103-3.R
- Fixed file list owned by package.

* Fri Feb 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3103-2.R
- Fixed SPEC. Updated to 3.0.3103-2.

* Thu Feb 11 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3103-1.R
- Updated SPEC to latest Sublime Text 3 version.

* Thu Nov 19 2015 Arkady L. Shane <ashejn@russiandedora.pro> - 3.0.3083-2.R
- fix issue with copyrights http://github.com/RussianFedora/sublime_text/issues/1
- rename spec
- define version in Obsoletes

* Mon Nov 16 2015 Arkady L. Shane <ashejn@russiandedora.pro> - 3.0.3083-1.R
- merge spec from karter <fp.karter@gmail.com>

* Sat Jan 24 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3083-1.R
- Updated SPEC for Sublime Text 3 support.

* Sun Dec 21 2014 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.2-1.R
- Updated SPEC and desktop files for openSUSE 13.2 and Fedora 21+ support.
