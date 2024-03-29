Name:		texlive-barr
Version:	38479
Release:	2
Summary:	Diagram macros by Michael Barr
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/barr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Diagxy is a general diagramming package, useful for diagrams in
a number of mathematical disciplines. Diagxy is a development
of an earlier (successful) package to use the facilities of the
xypic bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/barr
%doc %{_texmfdistdir}/doc/generic/barr

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
