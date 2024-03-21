# Studio CLI

[![Build APK package](https://github.com/atomic-studio-org/cli/actions/workflows/apk-package.yml/badge.svg)](https://github.com/atomic-studio-org/cli/actions/workflows/apk-package.yml)
[![Publish every Git push to main to FlakeHub](https://github.com/atomic-studio-org/cli/actions/workflows/flakehub-push.yml/badge.svg)](https://github.com/atomic-studio-org/cli/actions/workflows/flakehub-push.yml)

This project is meant for [Universal Blue](https://universal-blue.org/)-based systems, specifically the [Atomic Studio](https://github.com/atomic-studio-org/Atomic-Studio) image, but you can use it on any other system through the RPM, APK or Nix packages provided.

This utility manages your system by using commands like `studio manager install -m brew package` or other things related to audio, check out `studio -h` for a more extensive list of commands.

- Note: This CLI is still in an alpha stage, expect breakages and unreliable interfaces for now.

## Usage

This is the `--help` output as of writing:

```shell
The main Atomic Studio CLI.
You can use this to run Atomic Studio-specific commands

Usage:
  > studio 

Subcommands:
  studio manager - Available package managers: ["apt", "brew", "nix", "dnf", "yum", "paru", "pacman", "pipx"]
  studio manager export - Export selected packages from selected subsystem to the host system
  studio manager install - Add a package to your Atomic Studio system by using package subsystems or host-based package managers.
  studio manager remove - Remove a package to your Atomic Studio package subsystems or host-based package managers.
  studio motd - Display current MOTD text
  studio motd off - Turn MOTD off
  studio motd on - Turn MOTD on
  studio pw - Manage pipewire configurations
  studio pw disable realtime - Disables realtime from linux kernel arguments
  studio pw enable realtime - Enables realtime in linux kernel arguments
  studio pw reset config - Reset the entire custom pipewire configuration
  studio pw reset quantum-buffersize - Reset PIPEWIRE_QUANTUM variable back to its default 
  studio pw set config - Edit your own custom configuration for pipewire
  studio pw set quantum-buffersize - Set specific buffersize for PIPEWIRE_QUANTUM variable (fixes ardour and carla crashes)
  studio reporter - Report system information to facilitate Atomic Studio development
  studio reporter list - List all available modules to export
  studio setup - Setup Atomic Studio supported apps
  studio setup install amd-lact - Set up LACT, an overclocking utility for AMD cards
  studio setup install davinci - Install Davinci Resolve in a compatible distrobox
  studio setup install opentabletdriver - Install OpenTabletDriver in a container
  studio setup install rtcqs - Installs RTCQS in the host system for checking realtime perms
  studio setup install supergfxctl - This only works for Nvidia!
Enable Supergfxctl, a GPU switcher for hybrid laptops
  studio setup remove amd-lact - Uninstall LACT, an overclocking utility for AMD cards
  studio setup remove davinci - Delete Davinci Resolve in a from a distrobox
  studio setup remove opentabletdriver - Removes OpenTabletDriver services and the installation from container (does not delete the container itself.)
  studio setup remove rtcqs - Removes RTCQS from the host system
  studio setup remove supergfxctl - Disable Supergfxctl, a GPU switcher for hybrid laptops
  studio speaker-test - Test your speakers with espeak
  studio update - Run topgrade transaction for general upgrades
  studio update auto off - Disable automatic updates
  studio update auto on - Enable automatic updates
  studio update changelog - Show changelogs for the current system
  studio update pin - Pin a certain system version
  studio update rollback - Rollback an update 
  studio update unpin - Unpin a certain system version
  studio wine - 
  studio wine init - Workaround if your wine64 prefix is not working
  studio wine manager - Open the wine manager 
  studio wine run - Run anything through wine-tkg
  studio wine wineasio register - Register pipewire-wineasio DLL to default wine prefix
  studio wine wineasio unregister - Unregister pipewire-wineasio DLL to default wine prefix
  studio wine yabridge add - Scans a wine prefix for VSTPlugins folders
  studio wine yabridge scan - Scans a wine prefix for VSTPlugins folders
  studio wine yabridge sync - Sync yabridgectl database 

Flags:
  -h, --help - Display the help message for this command

Input/output types:
  ╭───┬───────┬────────╮
  │ # │ input │ output │
  ├───┼───────┼────────┤
  │ 0 │ any   │ any    │
  ╰───┴───────┴────────╯
```
