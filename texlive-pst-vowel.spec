Name:		texlive-pst-vowel
Version:	25228
Release:	2
Summary:	Enable arrows showing diphthongs on vowel charts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-vowel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vowel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vowel.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
