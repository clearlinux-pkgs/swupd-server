#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-server
Version  : 3.2.7
Release  : 23
URL      : https://github.com/clearlinux/swupd-server/releases/download/v3.2.7/swupd-server-3.2.7.tar.gz
Source0  : https://github.com/clearlinux/swupd-server/releases/download/v3.2.7/swupd-server-3.2.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: swupd-server-bin
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(bsdiff)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : xz-dev

%description
The swupd-server package provides a reference implementation of a software
update server-side component that generates update content consumable by a
software update client (swupd-client). Such content includes manifests that
describe incremental changes in the OS from build to build, binary deltas,
full copies of files (fullfiles) that were added/changed from a previous
build, and packs composed of binary deltas and/or fullfiles.

%package bin
Summary: bin components for the swupd-server package.
Group: Binaries

%description bin
bin components for the swupd-server package.


%prep
%setup -q -n swupd-server-3.2.7

%build
export LANG=C
%configure --disable-static --disable-tests
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swupd_create_update
/usr/bin/swupd_make_fullfiles
/usr/bin/swupd_make_pack
