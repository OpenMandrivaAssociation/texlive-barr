%global tl_name barr
%global tl_revision 38479

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Diagram macros by Michael Barr
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/diagrams/diagxy
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/barr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/barr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Diagxy is a general diagramming package, useful for diagrams in a number
of mathematical disciplines. Diagxy is a development of an earlier
(successful) package to use the facilities of the xypic bundle.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/barr
%dir %{_datadir}/texmf-dist/tex/generic/barr
%doc %{_datadir}/texmf-dist/doc/generic/barr/README
%doc %{_datadir}/texmf-dist/doc/generic/barr/diaxydoc.pdf
%doc %{_datadir}/texmf-dist/doc/generic/barr/diaxydoc.tex
%{_datadir}/texmf-dist/tex/generic/barr/diagxy.tex
