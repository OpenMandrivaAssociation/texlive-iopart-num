Name:		texlive-iopart-num
Version:	15878
Release:	1
Summary:	Numeric citation style for IOP journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/iopart-num
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iopart-num.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iopart-num.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A BibTeX style providing numeric citation in Harvard-like
format. Intended for use with Institute of Physics (IOP)
journals, including Journal of Physics.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/iopart-num/iopart-num.bst
%doc %{_texmfdistdir}/doc/bibtex/iopart-num/README
%doc %{_texmfdistdir}/doc/bibtex/iopart-num/iopart-num.bib
%doc %{_texmfdistdir}/doc/bibtex/iopart-num/iopart-num.pdf
%doc %{_texmfdistdir}/doc/bibtex/iopart-num/iopart-num.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
