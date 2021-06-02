# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
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

[unreleased]: https://github.com/tillsteinbach/WeConnect-cli/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.4.0
[0.3.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.3.1
[0.3.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.3.0
[0.2.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.2.1
[0.2.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.2.0
[0.1.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.1.0
