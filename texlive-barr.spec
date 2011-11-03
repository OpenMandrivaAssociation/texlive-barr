# revision 23579
# category Package
# catalog-ctan /macros/generic/diagrams/barr
# catalog-date 2011-06-19 14:02:49 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-barr
Version:	20110619
Release:	1
Summary:	Diagram macros by Michael Barr
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/barr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Diagxy is a general diagramming package, useful for diagrams in
a number of mathematical disciplines. Diagxy is a development
of an earlier (successful) package to use the facilities of the
xypic bundle.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/barr/diagxy.tex
%doc %{_texmfdistdir}/doc/generic/barr/diaxydoc.pdf
%doc %{_texmfdistdir}/doc/generic/barr/diaxydoc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
