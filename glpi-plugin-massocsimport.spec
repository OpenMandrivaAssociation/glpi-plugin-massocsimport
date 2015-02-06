%if %mandriva_branch == Cooker
%define release 3
%else
%define subrel 1
%define release 1
%endif

Summary: GLPI Plugin for OCS Massive import
Name: glpi-plugin-massocsimport
Version: 1.5.2
Release: %{release}
Group: Monitoring
License: GPLv2
URL: https://forge.indepnet.net/projects/show/massocsimport
Source0: https://forge.indepnet.net/attachments/download/975/glpi-massocsimport-%{version}.tar.gz
Requires: glpi >= 0.80
Requires: cronie
Provides: glpi-massocsimport = %{version}-%{release}
Obsoletes: glpi-massocsimport
BuildArch: noarch

%description
Plugin which allow OCS continuous synchronization and massive importation.

The extension Config panel is provided to handle the synchronization options.

%prep

%setup -q -n massocsimport

find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%build
# empty build

cat >cron <<EOF
# GLPI mass_ocs_import extension.
# Must be enabled from the Control panel.
*/5 * * * * apache %{_datadir}/glpi/plugins/massocsimport/scripts/ocsng_fullsync.sh
EOF

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/massocsimport
cp -rp * %{buildroot}%{_datadir}/glpi/plugins/massocsimport/

chmod 755 %{buildroot}%{_datadir}/glpi/plugins/massocsimport/scripts/ocsng_fullsync.sh

install -d %{buildroot}%{_sysconfdir}/cron.d
install -m0644 cron %{buildroot}%{_sysconfdir}/cron.d/%{name}

%files
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_datadir}/glpi/plugins/massocsimport


%changelog
* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-2mdv2012.0
+ Revision: 771130
- various fixes

* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-1
+ Revision: 771119
- import glpi-plugin-massocsimport


* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-1
- 1.5.2
- forward port from mes5.2 (the black hole) and with adjustments

* Sun Aug 14 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-0.1mdvmes5.2
- 1.4.2

* Mon May 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-3.1mdvmes5.2
- built for updates

* Mon Feb 14 2011 Leonardo Coelho <leonardoc@mandriva.com.br> 1.3.0-3mdvmes5.1
- fix cron path.

* Wed Jun 09 2010 Anne Nicolas <anne.nicolas@mandriva.com> 1.3.0-2mdvmes5
- fix plugin directory name

* Thu Feb 18 2010 Tiago Salem Herrmann <salem@mandriva.com> 1.3.0-1mdvmes5
- first build for MES5
