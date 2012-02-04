Summary:        GLPI Plugin for OCS Massive import
Name:           glpi-plugin-massocsimport
Version:        1.5.2
Release:        %mkrel 1
Group:          Monitoring
License:        GPLv2
URL:            https://forge.indepnet.net/projects/show/massocsimport
Source0:        https://forge.indepnet.net/attachments/download/975/glpi-massocsimport-%{version}.tar.gz
BuildArch:      noarch
Requires:       glpi >= 0.80
Requires:       cronie
Provides:	glpi-massocsimport = %{version}-%{release}
Obsoletes:	glpi-massocsimport
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/massocsimport
cp -rp * %{buildroot}%{_datadir}/glpi/plugins/massocsimport/

chmod 755 %{buildroot}%{_datadir}/glpi/plugins/massocsimport/scripts/ocsng_fullsync.sh

install -d %{buildroot}%{_sysconfdir}/cron.d
install -m0644 cron %{buildroot}%{_sysconfdir}/cron.d/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_datadir}/glpi/plugins/massocsimport

