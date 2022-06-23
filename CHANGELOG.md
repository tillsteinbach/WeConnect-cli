# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
- No unreleased changes so far

## [0.30.1] - 2022-06-23
### Added
- Added new values for attribute externalPower: active
- Added new values for attribute ledColor: green, red

### Changed
- Updated API to 0.43.1

## [0.30.0] - 2022-06-22 (Happy birthday Peer!)
### Added
- Added new attributes: externalPower, brandCode, autoUnlockPlugWhenChargedAC, ledColor (warning, it is not yet clear what values are allowed, so use these with caution)

### Changed
- Updated API to 0.43.0

## [0.29.0] - 2022-06-12
### Changed
- Updated API to 0.41.0

### Added
- selective allCapable added to only fetch data that is provided by the car

### Fixed
- Errors in domains are catched and do not produce warnings anymore

## [0.28.0] - 2022-05-12
### Changed
- Updated API to 0.40.0

## [0.27.0] - 2022-04-12
### Added
- Support for warning lights including png icons

### Changed
- Updated API to 0.39.0

## [0.26.1] - 2022-03-22
### Changed
- Improved error messages on login errors
- Updated API to 0.38.1

## [0.26.0] - 2022-03-19
### Added
- Added BatteryPowerLevel 'off' in readiness status.
- Added ClimatizationStatus 'invalid'
- Added occurringOn and startTime in singe timer

### Changed
- Updated API to 0.38.0

## [0.25.2] - 2022-03-04
### Fixed
- Catch error when server is not responding correctly during login

### Changed
- Updated API to 0.37.2

## [0.25.1] - 2022-02-28
### Fixed
- Bug in charging control

### Changed
- Updated API to 0.37.1

## [0.25.0] - 2022-02-25
### Fixed
- Requests tracking behaviour
- Catch error when token could not be fetched

### Changed
- Requests changed from list to dict
- Updated API to 0.37.0

### Added
- Possibility to use temperature when startng climatisation
- Added fail_no_external_power to generic request status
- Added chargeType attribute to chargingStatus
- Added chargingSettings attribute to chargingStatus

## [0.24.2] - 2022-02-12
### Fixed
- Fixes bug in charging state API fixing procedure

### Changed
- Updated API to 0.36.4

## [0.24.1] - 2022-02-11
### Fixed
- Login to WeConnect works again after changes on login page
- Fixes json output for values that are zero
- Fixes for chargePower, chargeRate and remaining climatisationTime

### Changed
- Updated API to 0.36.3

## [0.24.0] - 2022-02-03
### Added
- Possibility to output and save json format for the whole or parts of the tree
- Attributes for automation/chargingProfiles
- Added status fail_charge_plug_not_connected

### Changed
- Refactors the OAuth procedure
- Updated API to 0.36.0

## [0.23.2] - 2022-01-28
### Fixed
- Login to WeConnect works again after changes on login page

### Changed
- Updated API to 0.35.1

## [0.23.1] - 2022-01-24
### Fixed
- Small bugfixes

### Changed
- Updated API to 0.35.0

## [0.23.0] - 2022-01-23
### Changed
- All selective topics are now under "domains" section (Warning! This is a breaking change!)
- Updated API to 0.34.0

## [0.22.7] - 2022-01-18
### Fixed
- Add new tags attribute

### Changed
- Updated API to 0.33.0

## [0.22.6] - 2022-01-17
### Fixed
- Fixed a problem where the temperature of the climatization is always set to 20.5 C

### Changed
- Updated API to 0.32.1

## [0.22.5] - 2022-01-14
### Fixed
- Change datatype for chargePower_kW and chargeRate_kmph from Integer to Float

### Changed
- Updated API to 0.32.0

## [0.22.4] - 2022-01-12
### Fixed
- Fix problem with stored tokens
- Hide 504 gateway_timeout error on missing parking position

### Changed
- Updated API to 0.30.4

## [0.22.3] - 2022-01-11
### Fixed
- More robust against server errors
- Hides status 204 on missing parking position

### Changed
- Updated API to 0.30.3

## [0.22.2] - 2022-01-10
### Fixed
- timezone problem fixed

### Changed
- Updated API to 0.30.2

## [0.22.1] - 2022-01-10
### Fixed
- missing init file in API

### Changed
- Updated API to 0.30.1

## [0.22.0] - 2022-01-10
### Fixed
- no-capabilities fixed

### Added
- selective option that allows to only fetch a subset of the data

### Changed
- Updated API to 0.30.0

## [0.21.0] - 2022-01-05
### Changed
- ***Warning, the addresses of attributes changed due to conflicts within the status names from recent changes at WeConnect***
- API is using new url enpoints now
- Updated API to 0.29.0

### Fixed
- Conflicts when simplejson is installed and preferred from requests

### Added
- Added MBB Platform
- New logging configuration parameters

## [0.20.0] - 2021-12-20
### Added
- decoding of capability status
- new charge modes
- new plug states
- new engine and car types
- new status capabilitiesStatus

### Changed
- Only fetch parking position if the capability is enabled
- Updated API to 0.28.0

## [0.19.0] - 2021-12-08
### Added
- Add new gasoline car type

## [0.18.1] - 2021-12-01
### Fixed
- Fixed missing readiness_status module
### Changed
- Updated API to 0.25.1

## [0.18.0] - 2021-12-01
### Added
- Add new status fail_battery_low
- Add new attributes readinessStatus, readinessBatterySupportStatus and devicePlatform

### Changed
- Updated API to 0.25.0

## [0.17.0] - 2021-11-25
### Added
- Add new Charging State CHARGE_PURPOSE_REACHED_CONSERVATION

### Changed
- Updated API to 0.24.0

## [0.16.1] - 2021-11-19
### Fixed
- Corrected addressing of climatization timers

### Changed
- Updated API to 0.23.1

## [0.16.0] - 2021-11-19
### Added
- Add new Charging State CHARGE_PURPOSE_REACHED_NOT_CONSERVATION_CHARGING

### Changed
- Updated API to 0.23.0

## [0.15.4] - 2021-11-04
### Changed
- Updated API to 0.22.1

## [0.15.3] - 2021-11-01
### Changed
- Updated API to 0.22.0

## [0.15.2] - 2021-10-22
### Fixed
- Fix badge for unlocked vehicle
- Fixes return None for elapsed statistics if no statistics are available
- Fixes picture caching
- Will delete cache file if cache is corrupted

### Changed
- Updated API to 0.21.5

## [0.15.1] - 2021-10-06
### Fixed
- Will delete cache file if cache is corrupted

### Changed
- Updated API to 0.21.1

## [0.15.0] - 2021-10-06
### Added
- Statistics about retrieval times

### Fixed
- Climate settings and start stop

### Changed
- Updated API to 0.21.0

## [0.14.14] - 2021-09-28
### Fixed
- Fixed badges

## [0.14.13] - 2021-09-27
### Fixed
- Fixed resetting of parkingposition while driving

### Added
- New attributes: electricRange, gasolineRange

### Changed
- API updated to 0.20.14

## [0.14.12] - 2021-09-23
### Fixed
- Fixed problems coming from changes in the API

### Added
- New images with badges
- New attributes: odometerMeasurement, rangeMeasurements, unitInCar, targetTemperature_F

### Changed
- API updated to 0.20.12

## [0.14.11] - 2021-09-16
### Fixed
- Fixes previous release that did not take new exceptions into account

## [0.14.10] - 2021-09-15
### Added
- Will retry a request 3 times to try to make instable server connection more stable

### Fixed
- Problem when token could not be refreshed

### Changed
- API updated to 0.20.10

## [0.14.9] - 2021-09-10
### Fixed
- Fix if range is corrupted

## [0.14.8] - 2021-09-02
### Fixed
- Allow forbidden (403) return code for parking position
- Continue fetching data even if retrieval for one car fails

### Changed
- API version to 0.20.6

## [0.14.7] - 2021-09-02
### Fixed
- Fixed UnboundLocalError in condition GDC_MISSING

### Changed
- API version to 20.5

## [0.14.6] - 2021-09-01
### Fixed
- typing error on python 3.7

### Changed
- API version to 20.4

## [0.14.5] - 2021-08-30
### Fixed
- Display of consent url fixed

### Added
- Added new error state delayed

### Changed
- API version to 20.3

## [0.14.4] - 2021-08-26
### added
- New error messages for parking position
- New error state: fail_ignition_on

### Changed
- API version to 20.2

## [0.14.3] - 2021-08-25
### Added
- New error state: fail_vehicle_is_offline
- New status: climatisationSettingsRequestStatus

### Changed
- API version to 19.3

## [0.14.2] - 2021-08-20
### Fixed
- Fixed bad gateway error with parking position when car is driving

### Changed
- API version to 19.2

## [0.14.1] - 2021-08-19
### Fixed
- Parking position after weconnect API change

### Changed
- API version to 19.1

## [0.14.0] - 2021-08-15
### Added
- Possibility to set caching time for picture downloads seperately

### Changed
- Longer caching (24h default) for picture downloads

## [0.13.2] - 2021-08-14
### Fixed
- Bug when downloading pictures fails

### Changed
- Better output of version (adds WeConnect-python version to string)
- Updated API to 0.18.3

## [0.13.1] - 2021-07-30
### Fixed
- Fixes charging and climatization controls

### Changed
- Increase API version to 0.15

## [0.13.0] - 2021-07-28
### Added
- Added invalid WindowHeatingState
- Added invalid ChargeMode
- New statuses lvBatteryStatus (seen for ID vehicles), maintenanceStatus for legacy cars (contains milage and km/days until service) added

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

[unreleased]: https://github.com/tillsteinbach/WeConnect-cli/compare/v0.30.1..HEAD
[0.30.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.30.1
[0.30.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.30.0
[0.29.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.29.0
[0.28.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.28.0
[0.27.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.27.0
[0.26.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.26.1
[0.26.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.26.0
[0.25.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.25.2
[0.25.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.25.1
[0.25.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.25.0
[0.24.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.24.2
[0.24.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.24.1
[0.24.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.24.0
[0.23.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.23.2
[0.23.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.23.1
[0.23.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.23.0
[0.22.7]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.22.7
[0.22.6]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.22.6
[0.22.5]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.22.5
[0.22.4]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.22.4
[0.22.3]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.22.3
[0.22.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.22.2
[0.22.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.22.1
[0.22.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.22.0
[0.21.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.21.0
[0.20.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.20.0
[0.19.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.19.0
[0.18.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.18.1
[0.18.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.18.0
[0.17.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.17.0
[0.16.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.16.1
[0.16.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.16.0
[0.15.4]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.15.4
[0.15.3]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.15.3
[0.15.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.15.2
[0.15.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.15.1
[0.15.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.15.0
[0.14.14]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.14
[0.14.13]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.13
[0.14.12]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.12
[0.14.11]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.11
[0.14.10]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.10
[0.14.9]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.9
[0.14.8]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.8
[0.14.7]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.7
[0.14.6]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.6
[0.14.5]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.5
[0.14.4]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.4
[0.14.3]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.3
[0.14.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.2
[0.14.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.1
[0.14.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.14.0
[0.13.2]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.13.2
[0.13.1]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.13.1
[0.13.0]: https://github.com/tillsteinbach/WeConnect-cli/releases/tag/v0.13.0
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
