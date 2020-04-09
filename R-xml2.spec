#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xml2
Version  : 1.3.1
Release  : 75
URL      : https://cran.r-project.org/src/contrib/xml2_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xml2_1.3.1.tar.gz
Summary  : Parse XML
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-xml2-lib = %{version}-%{release}
Requires: R-curl
Requires: R-httr
BuildRequires : R-curl
BuildRequires : R-httr
BuildRequires : buildreq-R
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
# xml2
<!-- badges: start -->
[![R build status](https://github.com/r-lib/xml2/workflows/R-CMD-check/badge.svg)](https://github.com/r-lib/xml2/actions)
[![Travis Build Status](https://travis-ci.org/r-lib/xml2.svg?branch=master)](https://travis-ci.org/r-lib/xml2)
[![Coverage Status](https://img.shields.io/codecov/c/github/r-lib/xml2/master.svg)](https://codecov.io/github/r-lib/xml2?branch=master)
<!-- badges: end -->

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
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586450848

%install
export SOURCE_DATE_EPOCH=1586450848
rm -rf %{buildroot}
export LANG=C.UTF-8
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc xml2 || :


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
/usr/lib64/R/library/xml2/tests/testthat.R
/usr/lib64/R/library/xml2/tests/testthat/helper-version.R
/usr/lib64/R/library/xml2/tests/testthat/helper.R
/usr/lib64/R/library/xml2/tests/testthat/lego.html.bz2
/usr/lib64/R/library/xml2/tests/testthat/ns-multiple-aliases.xml
/usr/lib64/R/library/xml2/tests/testthat/ns-multiple-default.xml
/usr/lib64/R/library/xml2/tests/testthat/ns-multiple-prefix.xml
/usr/lib64/R/library/xml2/tests/testthat/ns-multiple.xml
/usr/lib64/R/library/xml2/tests/testthat/output/html_structure.txt
/usr/lib64/R/library/xml2/tests/testthat/output/print-xml_document.txt
/usr/lib64/R/library/xml2/tests/testthat/output/print-xml_node.txt
/usr/lib64/R/library/xml2/tests/testthat/output/print-xml_nodeset.txt
/usr/lib64/R/library/xml2/tests/testthat/records.dtd
/usr/lib64/R/library/xml2/tests/testthat/records.xml
/usr/lib64/R/library/xml2/tests/testthat/test-as_list.R
/usr/lib64/R/library/xml2/tests/testthat/test-as_xml_document.R
/usr/lib64/R/library/xml2/tests/testthat/test-cdata.R
/usr/lib64/R/library/xml2/tests/testthat/test-comment.R
/usr/lib64/R/library/xml2/tests/testthat/test-dtd.R
/usr/lib64/R/library/xml2/tests/testthat/test-format.R
/usr/lib64/R/library/xml2/tests/testthat/test-modify-xml.R
/usr/lib64/R/library/xml2/tests/testthat/test-namespaces.R
/usr/lib64/R/library/xml2/tests/testthat/test-null.R
/usr/lib64/R/library/xml2/tests/testthat/test-print.R
/usr/lib64/R/library/xml2/tests/testthat/test-read-xml.R
/usr/lib64/R/library/xml2/tests/testthat/test-url.R
/usr/lib64/R/library/xml2/tests/testthat/test-write_xml.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_attrs.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_children.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_find.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_missing.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_name.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_nodeset.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_parse.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_schema.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_serialize.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_structure.R
/usr/lib64/R/library/xml2/tests/testthat/test-xml_text.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/xml2/libs/xml2.so
