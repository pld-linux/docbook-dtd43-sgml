%define ver	4.3
%define sver	43
Summary:	DocBook 4.3 SGML - DTD for technical documentation
Summary(pl.UTF-8):	DocBook 4.3 SGML - DTD przeznaczone do pisania dokumentacji technicznej
Name:		docbook-dtd%{sver}-sgml
Version:	1.0
Release:	2
License:	Free
Group:		Applications/Publishing/SGML
Source0:	http://www.oasis-open.org/docbook/sgml/%{ver}/docbook-%{ver}.zip
# Source0-md5:	e3beb1b0b2923c24fa55a68e88654b01
URL:		http://www.oasis-open.org/docbook/
BuildRequires:	unzip
Requires(post,postun):	sgml-common >= 0.5
Requires:	sgml-common >= 0.5
Requires:	sgmlparser
Provides:	docbook-dtd
Obsoletes:	docbook%{sver}-dtd
Obsoletes:	docbook-sgml-%{ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DocBook 4.3 SGML - DTD for technical documentation.

%description -l pl.UTF-8
DocBook DTD jest zestawem definicji dokumentów przeznaczonych do
tworzenia dokumentacji programistycznej. Stosowany jest do pisania
podręczników systemowych, instrukcji technicznych jak i wielu innych
ciekawych rzeczy. Ten pakiet zawiera wersję DocBook 4.3 SGML.

%prep
%setup -q -c
chmod 644 *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}

install *.dtd *.mod *.dcl $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}

# install catalog (but filter out ISO entities)
grep -Ev '^(PUBLIC "ISO| *"iso-)' docbook.cat > $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}/catalog

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep -q /etc/sgml/sgml-docbook-%{ver}.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%postun
if [ "$1" = "0" ] ; then
	/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_datadir}/sgml/docbook/sgml-dtd-4.3
