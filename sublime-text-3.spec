# Let's disable compilation of Python scripts and modules and debug packages.
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%define debug_package %{nil}

Name: sublime_text
Version: 3.0
Release: 3083
Group: Applications/Editors
%ifarch x86_64
Source: http://c758482.r82.cf2.rackcdn.com/%{name}_3_build_%{release}_x64.tar.bz2
%else
Source: http://c758482.r82.cf2.rackcdn.com/%{name}_3_build_%{release}_x32.tar.bz2
%endif
Summary: Sublime Text 3
URL: http://www.sublimetext.com/3
License: EULA
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Sublime Text Authors
Requires: glib2
Requires: glibc
Requires: libX11
Requires: libXau
Requires: libffi
Requires: libgcc
Requires: libstdc++
Requires: libxcb
Requires: pcre
Requires: zlib
Obsoletes: sublimetext

%description
Sublime Text 3 for GNU/Linux is a sophisticated text editor for code, markup and prose.

%prep
%setup -q -c -n %{name}

%build
# Do nothing...

%install
# Unpacking...
rm -rf %{buildroot}

# Creating general directories...
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/opt/%{name}/

# Installing to working directory from official package...
mv "%_builddir/%{name}/sublime_text_3" %_builddir/%{name}/%{name}
cp -fpr %_builddir/%{name}/%{name}/* %{buildroot}/opt/%{name}/
rm -f %{buildroot}/opt/%{name}/sublime_text.desktop
chmod +x %{buildroot}/opt/%{name}/sublime_text

# Creating desktop icon...
echo "[Desktop Entry]" > %{buildroot}/usr/share/applications/%{name}.desktop
echo "GenericName=Text Editor" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "GenericName[ru]=Текстовый редактор" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Name=Sublime Text 3" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Name[ru]=Sublime Text 3" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Comment=Edit text files" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Exec=/opt/%{name}/sublime_text" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Icon=/opt/%{name}/Icon/256x256/sublime-text.png" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Terminal=false" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Type=Application" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Encoding=UTF-8" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "Categories=Utility;TextEditor;" >> %{buildroot}/usr/share/applications/%{name}.desktop
echo "MimeType=text/plain;text/x-c++src;text/x-c++hdr;text/x-xsrc;text/html;text/javascript;text/php;text/xml;" >> %{buildroot}/usr/share/applications/%{name}.desktop

# Generating list of files...
find %{buildroot} -not -type d -printf "\"/%%P\"\n" | sed '/\/man\//s/$/\*/' > manifest

%files -f manifest

%changelog
* Mon Jun 15 2015 karter <fp.karter@gmail.com>
- Updated SPEC for Sublime Text 3.

