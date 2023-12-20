Name:		texlive-statistics
Version:	67201
Release:	1
Summary:	Compute and typeset statistics tables and graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/statistics
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistics.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistics.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The 'statistics' package can compute and typeset statistics
like frequency tables, cumulative distribution functions
(increasing or decreasing, in frequency or absolute count
domain), from the counts of individual values, or ranges, or
even the raw value list with repetitions. It can also compute
and draw a bar diagram in case of individual values, or, when
the data repartition is known from ranges, an histogram or the
continuous cumulative distribution function. You can ask
'statistics' to display no result, selective results or all of
them. Similarly 'statistics' can draw only some parts of the
graphs. Every part of the generated tables or graphics is
customizable.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/statistics
%{_texmfdistdir}/tex/latex/statistics
%doc %{_texmfdistdir}/doc/latex/statistics

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
