# revision 23579
# category Package
# catalog-ctan /macros/generic/diagrams/barr
# catalog-date 2011-06-19 14:02:49 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-barr
Version:	20110619
Release:	7
Summary:	Diagram macros by Michael Barr
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/barr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barr.doc.tar.xz
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
%{_texmfdistdir}/tex/generic/barr/diagxy.tex
%doc %{_texmfdistdir}/doc/generic/barr/diaxydoc.pdf
%doc %{_texmfdistdir}/doc/generic/barr/diaxydoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110619-2
+ Revision: 749449
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110619-1
+ Revision: 717883
- texlive-barr
- texlive-barr
- texlive-barr
- texlive-barr
- texlive-barr

