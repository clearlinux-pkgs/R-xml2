#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xml2
Version  : 0.1.2
Release  : 9
URL      : http://cran.r-project.org/src/contrib/xml2_0.1.2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/xml2_0.1.2.tar.gz
Summary  : Parse XML
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-xml2-lib
Requires: R-BH
Requires: R-Rcpp
Requires: R-testthat
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-testthat
BuildRequires : clr-R-helpers
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : zlib-dev

%description
# xml2
The xml2 package is a binding to [libxml2](http://xmlsoft.org), making it easy to work with HTML and XML from R. The API is somewhat inspired by [jQuery](http://jquery.com).

%package lib
Summary: lib components for the R-xml2 package.
Group: Libraries

%description lib
lib components for the R-xml2 package.


%prep
%setup -q -c -n xml2

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library xml2
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library xml2


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/xml2/DESCRIPTION
/usr/lib64/R/library/xml2/INDEX
/usr/lib64/R/library/xml2/Meta/Rd.rds
/usr/lib64/R/library/xml2/Meta/hsearch.rds
/usr/lib64/R/library/xml2/Meta/links.rds
/usr/lib64/R/library/xml2/Meta/nsInfo.rds
/usr/lib64/R/library/xml2/Meta/package.rds
/usr/lib64/R/library/xml2/NAMESPACE
/usr/lib64/R/library/xml2/R/xml2
/usr/lib64/R/library/xml2/R/xml2.rdb
/usr/lib64/R/library/xml2/R/xml2.rdx
/usr/lib64/R/library/xml2/extdata/r-project.html
/usr/lib64/R/library/xml2/help/AnIndex
/usr/lib64/R/library/xml2/help/aliases.rds
/usr/lib64/R/library/xml2/help/paths.rds
/usr/lib64/R/library/xml2/help/xml2.rdb
/usr/lib64/R/library/xml2/help/xml2.rdx
/usr/lib64/R/library/xml2/html/00Index.html
/usr/lib64/R/library/xml2/html/R.css
/usr/lib64/R/library/xml2/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/xml2/libs/xml2.so
