# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/iopart-num
# catalog-date 2009-01-27 15:17:42 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-iopart-num
Version:	2.1
Release:	1
Summary:	Numeric citation style for IOP journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/iopart-num
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iopart-num.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iopart-num.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A BibTeX style providing numeric citation in Harvard-like
format. Intended for use with Institute of Physics (IOP)
journals, including Journal of Physics.

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
%{_texmfdistdir}/bibtex/bst/iopart-num/iopart-num.bst
%doc %{_texmfdistdir}/doc/bibtex/iopart-num/README
%doc %{_texmfdistdir}/doc/bibtex/iopart-num/iopart-num.bib
%doc %{_texmfdistdir}/doc/bibtex/iopart-num/iopart-num.pdf
%doc %{_texmfdistdir}/doc/bibtex/iopart-num/iopart-num.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
