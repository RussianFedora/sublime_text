%global debug_package %{nil}
%global revision 3103

Name: sublime_text
Version: 3.0.%{revision}
Release: 2%{?dist}
Summary: Sublime Text 3

Source0: https://download.sublimetext.com/%{name}_3_build_%{revision}_x64.tar.bz2
Source1: https://download.sublimetext.com/%{name}_3_build_%{revision}_x32.tar.bz2
Source2: %{name}.desktop

URL: http://www.sublimetext.com/3
License: EULA

BuildRequires: desktop-file-utils
Obsoletes: sublimetext

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
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/opt/%{name}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{256x256,128x128,48x48,32x32,16x16}/apps/

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

# Marking as executtable...
chmod +x %{buildroot}/opt/%{name}/%{name}

# Creating desktop icon...
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%dir /opt/%{name}
/opt/%{name}/plugin_host
/opt/%{name}/%{name}
/opt/%{name}/python3.3.zip
/opt/%{name}/changelog.txt
/opt/%{name}/Packages/*.sublime-package
/opt/%{name}/sublime_plugin.py*
/opt/%{name}/sublime.py*
/opt/%{name}/crash_reporter
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Fri Feb 12 2016 V1TSK <vitaly@easycoding.org> - 3.0.3103-2
- Fixed SPEC.

* Thu Feb 11 2016 V1TSK <vitaly@easycoding.org> - 3.0.3103-1
- Updated SPEC to latest Sublime Text 3 version.

* Sat Jan 24 2015 V1TSK <vitaly@easycoding.org> - 3.0.3083-1
- Updated SPEC for Sublime Text 3 support.

* Sun Dec 21 2014 V1TSK <vitaly@easycoding.org> - 2.0.2-1
- Updated SPEC and desktop files for openSUSE 13.2 and Fedora 21+ support.
