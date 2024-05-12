Name:          studio-cli 
Vendor:        atomic-studio-org
Version:       0.1.0+{{{ git_ref }}}
Release:       0%{?dist}
Summary:       Manager for Atomic Studio
License:       3.0-BSD
URL:           https://github.com/%{vendor}/%{name}
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}

BuildArch:     noarch 
Supplements:   podman docker
Requires:      nu

%description
Manages Atomic Studio installations

%global debug_package %{nil}
%global pname studio

%prep
{{{ git_dir_setup_macro }}}

%build

%install
mkdir -p %{buildroot}%{_libexecdir}/studio-cli %{buildroot}/%{_bindir}
sed -i 's~\.\/libexec~\/usr\/libexec/%{name}~' src/%{pname}
cat src/%{pname}
install -D -m 0755 src/%{pname} %{buildroot}%{_bindir}/%{pname}
cp -r src/libexec/* %{buildroot}%{_libexecdir}/%{name}

%files
%license LICENSE
%{_libexecdir}/%{name}/*
%attr(0755,root,root) %{_bindir}/%{pname}

%changelog
%autochangelog
