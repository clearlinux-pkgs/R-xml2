#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xml2
Version  : 1.1.1
Release  : 33
URL      : http://cran.r-project.org/src/contrib/xml2_1.1.1.tar.gz
Source0  : http://cran.r-project.org/src/contrib/xml2_1.1.1.tar.gz
Summary  : Parse XML
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-xml2-lib
Requires: R-BH
Requires: R-Rcpp
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
# xml2
[![Build Status](https://travis-ci.org/hadley/xml2.svg?branch=master)](https://travis-ci.org/hadley/xml2)
[![Coverage Status](https://img.shields.io/codecov/c/github/hadley/xml2/master.svg)](https://codecov.io/github/hadley/xml2?branch=master)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/hadley/xml2?branch=master&svg=true)](https://ci.appveyor.com/project/hadley/xml2)

%package lib
Summary: lib components for the R-xml2 package.
Group: Libraries

%description lib
lib components for the R-xml2 package.


%prep
%setup -q -c -n xml2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492798613

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492798613
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xml2
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library xml2


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/xml2/DESCRIPTION
/usr/lib64/R/library/xml2/INDEX
/usr/lib64/R/library/xml2/Meta/Rd.rds
/usr/lib64/R/library/xml2/Meta/features.rds
/usr/lib64/R/library/xml2/Meta/hsearch.rds
/usr/lib64/R/library/xml2/Meta/links.rds
/usr/lib64/R/library/xml2/Meta/nsInfo.rds
/usr/lib64/R/library/xml2/Meta/package.rds
/usr/lib64/R/library/xml2/Meta/vignette.rds
/usr/lib64/R/library/xml2/NAMESPACE
/usr/lib64/R/library/xml2/NEWS.md
/usr/lib64/R/library/xml2/R/xml2
/usr/lib64/R/library/xml2/R/xml2.rdb
/usr/lib64/R/library/xml2/R/xml2.rdx
/usr/lib64/R/library/xml2/doc/index.html
/usr/lib64/R/library/xml2/doc/modification.R
/usr/lib64/R/library/xml2/doc/modification.Rmd
/usr/lib64/R/library/xml2/doc/modification.html
/usr/lib64/R/library/xml2/extdata/order-doc.xml
/usr/lib64/R/library/xml2/extdata/order-schema.xml
/usr/lib64/R/library/xml2/extdata/r-project.html
/usr/lib64/R/library/xml2/help/AnIndex
/usr/lib64/R/library/xml2/help/aliases.rds
/usr/lib64/R/library/xml2/help/paths.rds
/usr/lib64/R/library/xml2/help/xml2.rdb
/usr/lib64/R/library/xml2/help/xml2.rdx
/usr/lib64/R/library/xml2/html/00Index.html
/usr/lib64/R/library/xml2/html/R.css
/usr/lib64/R/library/xml2/include/xml2_types.h
/usr/lib64/R/library/xml2/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/xml2/libs/xml2.so
