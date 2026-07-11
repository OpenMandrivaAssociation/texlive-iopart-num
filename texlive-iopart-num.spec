%global tl_name iopart-num
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Numeric citation style for IOP journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/iopart-num
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iopart-num.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iopart-num.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A BibTeX style providing numeric citation in Harvard-like format.
Intended for use with Institute of Physics (IOP) journals, including
Journal of Physics.

