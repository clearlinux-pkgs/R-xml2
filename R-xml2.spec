#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xml2
Version  : 1.2.0
Release  : 42
URL      : https://cran.r-project.org/src/contrib/xml2_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xml2_1.2.0.tar.gz
Summary  : Parse XML
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-xml2-lib
Requires: R-Rcpp
Requires: R-curl
BuildRequires : R-Rcpp
BuildRequires : R-curl
BuildRequires : clr-R-helpers
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
top of the 'libxml2' C library.

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
export SOURCE_DATE_EPOCH=1522357104

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522357104
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xml2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xml2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xml2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library xml2|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/xml2/extdata/cd_catalog.xml
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
/usr/lib64/R/library/xml2/libs/xml2.so.avx2
/usr/lib64/R/library/xml2/libs/xml2.so.avx512
