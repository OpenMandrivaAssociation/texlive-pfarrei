%global tl_name pfarrei
%global tl_revision 68950
%global tl_bin_links a5toa4:%{_texmfdistdir}/scripts/pfarrei/a5toa4.tlu pfarrei:%{_texmfdistdir}/scripts/pfarrei/pfarrei.tlu

Name:		texlive-%{tl_name}
Epoch:		1
Version:	r37
Release:	%{tl_revision}.1
Summary:	LaTeX support of pastors and priests work
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pfarrei
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pfarrei.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pfarrei.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pfarrei.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pfarrei.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
In "Die TeXnische Komodie" (issue 1/2013) Christian Justen described his
use of LaTeX in his work as priest (similar requirements may be
encountered in the work of pastors and other ministers of religion). One
point was to arrange A5 pages onto A4 landscape paper, either side-by-
side or as a booklet. Justen made two bash scripts for this job; the
package provides one texlua script for both requirements. (Note that
file a5toa4.tlu should have execute permissions in any installation.)

