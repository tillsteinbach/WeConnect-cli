# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
- No unreleased changes so far

## [0.12.2] - 2021-07-26
### Changed
- Improved error message when user consent is missing
- More robust against server side errors when refreshing the tokens
- API updated to version 0.13.2

## [0.12.1] - 2021-07-26
### Fixed
- Import of subpackages

## [0.12.0] - 2021-07-26
### Added
- Dummy for maintenance status (currently no data provided, only error messages)
- Added attribute for chargeMode

### Changed
- More compact string formating
- Changed python API to 0.13.0

## [0.11.4] - 2021-07-25
### Fixed
- Fixed crash due to 404 error when retrieving parking position for cars that don't provide parking positions

## [0.11.3] - 2021-07-18
### Fixed
- Fixed crash due to new elements in the WeConnect API

## [0.11.2] - 2021-07-06
### Fixed
- Fixed --no-pictures argument

## [0.11.1] - 2021-07-06
### Changed
- Update API to 0.12.1 for minor bugfix

## [0.11.0] - 2021-07-05
### Added
- Support to work with car images / status images

## [0.10.2] - 2021-07-03
### Fixed
- Bug with addresses fixed in API 0.11.1
### Changed
- Update API to 0.11.1 to use charging station data

## [0.10.1] - 2021-07-02
### Fixed
- Bug when no location is provided

## [0.10.0] - 2021-07-02
### Added
- Ability to get data for charging stations

### Changed
- Update API to 0.11.0 to use charging station data

## [0.9.0] - 2021-06-28
### Changed
- Update API to 0.10.0 to use access token instead of id token
- More robust on connection problems with WeConnect servers

## [0.8.2] - 2021-06-21
### Fixed
- Fixed list and list -s command by updating API to 0.8.2
- Fixed missing fail status by updating API to 0.9.0

## [0.8.1] - 2021-06-21
### Fixed
- Wrong error message containing unused attribute

## [0.8.0] - 2021-06-21
### Added
- Support for chargeMode attribute by increasing API version to 0.8.0

## [0.7.0] - 2021-06-21
### Added
- Support for singleTimer attribute

## [0.6.2] - 2021-06-18
### Fixes
- Small bugfixes by updating API to 0.6.2

## [0.6.1] - 2021-06-13
### Fixes
- Fixes bug in observer by updating API to 0.6.1 (fixes #2)

## [0.6.0] - 2021-06-11
### Added
- Support for coUser attribute

### Changed
- Update of API to version 0.6.0

## [0.5.4] - 2021-06-10
### Changed
- API Version updated to 0.5.2 to fix bug with charging settings

## [0.5.3] - 2021-06-09
### Changed
- API Version updated to 0.5.1

### Fixed
- Fixes problem with recurring timer missing (#1)

## [0.5.2] - 2021-06-09
### Changed
- API Version updated to 0.5.0

## [0.5.1] - 2021-06-06
### Added
- Better suggestions for possible Enum values on set command

### Changed
- Updated to API version 0.4.1

## [0.5.0] - 2021-06-04
### Added
- Possibility to set attributes and control services
- New WeConnect shell for interactive working with weconnect (experimental)

## [0.4.0] - 2021-06-02
### Changed
- The default behaviour is now to always cache unless --no-cache is provided.
  The cache outdates after --interval seconds (default 300). The reason for this
  change is to not unncessesarily stress VW servers. Use --no-cache option with care.

## [0.3.1] - 2021-05-31
### Fixed
- Correct minimum required python version to 3.7
- Problems when using caching

## [0.3.0] - 2021-05-28
### Fixed
- Help text for cache file displaying correct default value
- Corrected name for logger
- Improved error messages for missing netrc files

### Added
- Default value for .netrc file path shown in help
- Improved error handling for login

## [0.2.1] - 2021-05-28
### Fixed
- Output when there is no command added

## [0.2.0] - 2021-05-27
### Added
- Possibility to cache data between calls

## [0.1.0] - 2021-05-26
Initial release

[unreleased]: https://github.com/tillsteinbach/WeConnect-cli/compare/v0.12.2..HEAD
[0.12.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.12.2
[0.12.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.12.1
[0.12.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.12.0
[0.11.4]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.11.4
[0.11.3]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.11.3
[0.11.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.11.2
[0.11.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.11.1
[0.11.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.11.0
[0.10.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.10.2
[0.10.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.10.1
[0.10.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.10.0
[0.9.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.9.0
[0.8.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.8.2
[0.8.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.8.1
[0.8.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.8.0
[0.7.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.7.0
[0.6.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.6.2
[0.6.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.6.1
[0.6.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.6.0
[0.5.4]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.5.4
[0.5.3]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.5.3
[0.5.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.5.2
[0.5.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.5.1
[0.5.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.5.0
[0.4.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.4.0
[0.3.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.3.1
[0.3.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.3.0
[0.2.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.2.1
[0.2.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.2.0
[0.1.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.1.0
