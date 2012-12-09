# revision 25228
# category Package
# catalog-ctan /macros/latex/contrib/pst-vowel
# catalog-date 2012-01-28 08:48:38 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pst-vowel
Version:	1.0
Release:	3
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

%description
The package extends vowel.sty (distributed as part of the tipa
bundle) by allowing the user to draw arrows between vowels to
show relationships such as diphthong membership. The package
depends on use of pstricks.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-vowel/pst-vowel.sty
%doc %{_texmfdistdir}/doc/latex/pst-vowel/README
%doc %{_texmfdistdir}/doc/latex/pst-vowel/pst-vowel.pdf
%doc %{_texmfdistdir}/doc/latex/pst-vowel/pst-vowel.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-3
+ Revision: 770238
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755503
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719406
- texlive-pst-vowel
- texlive-pst-vowel
- texlive-pst-vowel
- texlive-pst-vowel

