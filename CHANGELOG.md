# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2.5] - 2023-03-22
### Added
- Added support for configuration file `config.json`.

### Changed
- Minimum supported Python version is now 3.10.x.

### Fixed
- Fixed `systemd` timer not starting - needed to add more conditions for starting.
- Ensured that the database directory exists before executing the commands.

## [0.2.4] - 2023-03-16
### Changed
- In `main.py`, changed argument parsing from `sys.argv` to `argparse`.
    - Added an optional parameter for changing the default parent directory.
    - Using `argparse` defaults, removed an unnecessary check for the `users` argument.

### Fixed
- Fixed incorrect test check in `main.bash`.

## [0.2.3] - 2023-03-05
### Added
- Added `bootstrap.bash` for bootstrapping setup. It installs the virtual environment and places the new `systemd` service files into the `user` `systemd` location.
- Added `systemd` service and timer for automatic execution. Timer is currently set for 15 minutes. The service executes the new `main.bash` script, a wrapper around the virtual environment and `main.py`.

## [0.2.2] - 2022-12-11
### Security
- Bumped `certifi` to latest version.

## [0.2.1] - 2022-08-06
### Changed
- Fixed #1: moved database initialization block out of the loop.

## [0.2.0] - 2021-08-21
### Changed
- Replaced tz-naive `datetime` with `pendulum` to create RFC3339 strings.

## [0.1.0] - 2021-08-16
### Added
- Initial version
