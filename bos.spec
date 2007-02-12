Summary:	Invasion - Battle of Survival - a real-time strategy game using the Stratagus game engine
Summary(pl.UTF-8):   Invasion - Battle of Survival - strategia czasu rzeczywistego korzystającą z silnika Stratagus
Name:		bos
Version:	1.1
%define _ver 1_1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://bos.seul.org/files/%{name}_%{_ver}.tar.gz
# Source0-md5:	39e705ad6b4ae77e808cd88aabae361c
Source1:	bos-run_script
URL:		http://bos.seul.org/
Requires:	stratagus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Invasion - Battle of Survival is a real-time strategy game using the
Stratagus game engine.

%description -l pl.UTF-8
Invasion - Battle of Survival jest strategią czasu rzeczywistego
korzystającą z silnika Stratagus.

%prep
%setup -q -n %{name}_%{_ver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}

cp -dpR data/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/bos

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt 
%attr(755,root,root) %{_bindir}/bos
%{_datadir}/games/%{name}
