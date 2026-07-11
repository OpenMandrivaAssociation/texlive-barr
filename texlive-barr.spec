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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Diagxy is a general diagramming package, useful for diagrams in a number
of mathematical disciplines. Diagxy is a development of an earlier
(successful) package to use the facilities of the xypic bundle.

