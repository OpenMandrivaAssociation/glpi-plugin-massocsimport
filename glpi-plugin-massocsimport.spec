%if %mandriva_branch == Cooker
%define release %mkrel 2
%else
%define subrel 1
%define release %mkrel 0
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
