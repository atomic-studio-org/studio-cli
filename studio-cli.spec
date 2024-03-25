Name:          studio-cli 
Vendor:        atomic-studio-org
Version:       {{{ studio-cli_version }}}
Release:       0%{?dist}
Summary:       Manager for Atomic Studio
License:       Apache-2.0
URL:           https://github.com/%{vendor}/%{name}
# Detailed information about the source Git repository and the source commit
# for the created rpm package
VCS:           {{{ git_dir_vcs }}}

# git_dir_pack macro places the repository content (the source files) into a tarball
# and returns its filename. The tarball will be used to build the rpm.
Source:        {{{ git_dir_pack }}}

BuildArch:     noarch 
Supplements:   podman 
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
sed -i 's~\.\/libexec~\/usr\/libexec/~' src/%{pname}
install -D -m 0755 src/%{pname} %{buildroot}%{_bindir}/%{pname}
cp -r src/libexec/* %{buildroot}%{_libexecdir}/%{name}

%files
%license LICENSE
%{_libexecdir}/%{name}/*
%attr(0755,root,root) %{_bindir}/%{pname}

%changelog
%autochangelog
