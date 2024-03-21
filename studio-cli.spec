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

%description
Manages Atomic Studio installations

%global debug_package %{nil}
%global pname studio

%prep
{{{ git_dir_setup_macro }}}

%build

%install
mkdir -p %{_libexecdir}/studio-cli
install -D -m 0755 src/studio %{buildroot}%{_bindir}/%{pname}
cp -r src/libexec/* %{_libexecdir}/studio-cli

%files
%license LICENSE
%attr(0755,root,root) %{_bindir}/%{pname}

%changelog
%autochangelog
