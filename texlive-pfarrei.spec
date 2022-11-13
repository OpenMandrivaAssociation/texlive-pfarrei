Name:		texlive-pfarrei
Version:	31934
Release:	1
Summary:	LaTeX support of pastors' and priests' work
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pfarrei
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pfarrei.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pfarrei.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pfarrei.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pfarrei.bin = %{EVRD}

%description
In "Die TeXnische Komodie" (issue 1/2013) Christian Justen
described his use of LaTeX in his work as priest (similar
requirements may be encountered in the work of pastors and
other ministers of religion). One point was to arrange A5 pages
onto A4 landscape paper, either side-by-side or as a booklet.
Justen made two bash scripts for this job; the package provides
one texlua script for both requirements. (Note that file
a5toa4.tlu should have execute permissions in any
installation.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/a5toa4
%{_bindir}/pfarrei
%{_texmfdistdir}/scripts/pfarrei/a5toa4.tlu
%{_texmfdistdir}/scripts/pfarrei/pfarrei.tlu
%{_texmfdistdir}/tex/latex/pfarrei/a5toa4.tex
%{_texmfdistdir}/tex/latex/pfarrei/pfarrei.sty
%doc %{_texmfdistdir}/doc/latex/pfarrei/pfarrei.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pfarrei/README
%doc %{_texmfdistdir}/source/latex/pfarrei/pfarrei.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/pfarrei/a5toa4.tlu a5toa4
ln -sf %{_texmfdistdir}/scripts/pfarrei/pfarrei.tlu pfarrei
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
