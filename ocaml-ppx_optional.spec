#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Pattern matching on flat options
Summary(pl.UTF-8):	Dopasowywanie wzorców do płaskich opcji
Name:		ocaml-ppx_optional
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_optional/tags
Source0:	https://github.com/janestreet/ppx_optional/archive/v%{version}/ppx_optional-%{version}.tar.gz
# Source0-md5:	7c398967c245d8f35a3e8aa5165641e8
URL:		https://github.com/janestreet/ppx_optional
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx rewriter that rewrites simple match statements with an if then
else expression.

This package contains files needed to run bytecode executables using
ppx_optional library.

%description -l pl.UTF-8
Moduł przepisujący ppx, przepisujący proste instrukcje match na
wyrażenia if then else.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_optional.

%package devel
Summary:	Pattern matching on flat options - development part
Summary(pl.UTF-8):	Dopasowywanie wzorców do płaskich opcji - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_optional library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_optional.

%prep
%setup -q -n ppx_optional-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_optional/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_optional

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_optional
%attr(755,root,root) %{_libdir}/ocaml/ppx_optional/ppx.exe
%{_libdir}/ocaml/ppx_optional/META
%{_libdir}/ocaml/ppx_optional/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_optional/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_optional/*.cmi
%{_libdir}/ocaml/ppx_optional/*.cmt
%{_libdir}/ocaml/ppx_optional/*.cmti
%{_libdir}/ocaml/ppx_optional/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_optional/ppx_optional.a
%{_libdir}/ocaml/ppx_optional/*.cmx
%{_libdir}/ocaml/ppx_optional/*.cmxa
%endif
%{_libdir}/ocaml/ppx_optional/dune-package
%{_libdir}/ocaml/ppx_optional/opam
