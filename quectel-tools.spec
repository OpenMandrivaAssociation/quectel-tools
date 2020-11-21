Name:		quectel-tools
Version:	1.5
Release:	1
Summary:	Tools for working with Quectel cellular modems
# License says it's "Public Domain and Open Source for Quectel customers
# only", which is a bit of a contradiction in itself.
# We interpret this to mean "It's Open Source for Quectel customers and
# not distributed to anyone else", which gives Quectel customers, who
# receive the code as "Public Domain and Open Source" the right
# to redistribute and allow further redistribution.
License:	uncertain
# QLog allows internal tracing of the modem firmware
# Obtained from
# https://cnquectel-my.sharepoint.com/:f:/g/personal/europe-fae_quectel_com/EmuxQDS_WYhFsAttfULluywB8RK9znft_oAALHh8uPYNFg?e=3459qx
Source0:	Quectel_QLog_Linux&Android_V1.5.zip
Source1:	Quectel_LTE_QLog_Linux\&Android_User_Guide_V1.0.pdf
# QFirehose allows updating the firmware on Quectel modems
# https://forum.pine64.org/showthread.php?tid=11815
Source2:	https://universe2.us/collector/qfirehose_good.tar.zst
# Firmware files can be obtained e.g. at
# https://cnquectel-my.sharepoint.com/personal/europe-fae_quectel_com/_layouts/15/onedrive.aspx?originalPath=aHR0cHM6Ly9jbnF1ZWN0ZWwtbXkuc2hhcmVwb2ludC5jb20vOmY6L2cvcGVyc29uYWwvZXVyb3BlLWZhZV9xdWVjdGVsX2NvbS9FbXV4UURTX1dZaEZzQXR0ZlVMbHV5d0I4Uks5em5mdF9vQUFMSGg4dVBZTkZnP3J0aW1lPXNnTldWVU9PMkVn&id=%2Fpersonal%2Feurope%2Dfae%5Fquectel%5Fcom%2FDocuments%2FLukasz%2FEG25%2DG%5FLatest%5FFW
# https://github.com/Biktorgj/quectel_eg25_recovery
BuildRequires:	make

%description
Tools for working with Quectel modems

%prep
%autosetup -p1 -n QLog
# Wipe prebuilt binaries
%make_build clean
tar xf %{S:2}
cd qfirehose_good
%make_build clean

%build
%make_build CC=%{__cc} CFLAGS="%{optflags}"
cd qfirehose_good
%make_build CC=%{__cc} CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_docdir}/%{name}-%{version}
install -m 755 QLog %{buildroot}%{_bindir}/
install -m 755 qfirehose_good/QFirehose %{buildroot}%{_bindir}/
install -c -m 644 %{S:1} %{buildroot}%{_docdir}/%{name}-%{version}/

%files
%{_bindir}/QLog
%{_bindir}/QFirehose
%doc %{_docdir}/%{name}-%{version}
