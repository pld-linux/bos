Summary:	Invasion - Battle of Survival is a real-time strategy game using the Stratagus game engine.
Summary(pl):	Invasion - Battle of Survival jest strategi± czasu rzeczywistego korzystaj±c± z engine'u Stratagus.
Name:		bos
Version:	1.1
%define _ver 1_1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Games/Strategy
Vendor:		PLD
Source0:	http://www.nongnu.org/stratagus-bos/files/%{name}_%{_ver}.tar.gz
# Source0-md5:	39e705ad6b4ae77e808cd88aabae361c
Source1:	bos-run_script
# Source1-md5:	537e4726dc657cfcc2a5eaeb3d94efd8
URL:		http://www.nongnu.org/stratagus-bos/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Invasion - Battle of Survival is a real-time strategy game using the
Stratagus game engine.

%description -l pl
Invasion - Battle of Survival jest strategi± czasu rzeczywistego
korzystaj±c± z engine'u Stratagus.

%prep
%setup -q -n %{name}_%{_ver}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/games/%{name}
install -d $RPM_BUILD_ROOT/%{_bindir}
cp -dpR data/* $RPM_BUILD_ROOT/%{_datadir}/games/%{name}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/bos

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc README.txt 
%attr(755,root,root) %{_bindir}/bos
%{_datadir}/games/%{name}
