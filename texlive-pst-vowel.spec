%global tl_name pst-vowel
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Enable arrows showing diphthongs on vowel charts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-vowel
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vowel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vowel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the vowel package (distributed as part of the tipa
bundle) by allowing the user to draw arrows between vowels to show
relationships such as diphthong membership. The package depends on use
of pstricks.

