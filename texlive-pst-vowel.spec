# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pst-vowel
# catalog-date 2009-05-02 10:43:42 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pst-vowel
Version:	1.0
Release:	1
Summary:	Enable arrows showing diphthongs on vowel charts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-vowel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vowel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vowel.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package extends vowel.sty (distributed as part of the tipa
bundle) by allowing the user to draw arrows between vowels to
show relationships such as diphthong membership. The package
depends on use of pstricks.

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
%{_texmfdistdir}/tex/latex/pst-vowel/pst-vowel.sty
%doc %{_texmfdistdir}/doc/latex/pst-vowel/README
%doc %{_texmfdistdir}/doc/latex/pst-vowel/pst-vowel.pdf
%doc %{_texmfdistdir}/doc/latex/pst-vowel/pst-vowel.tex
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
