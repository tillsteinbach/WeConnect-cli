# WeConnect-cli
[![GitHub sourcecode](https://img.shields.io/badge/Source-GitHub-green)](https://github.com/tillsteinbach/WeConnect-cli/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/tillsteinbach/WeConnect-cli)](https://github.com/tillsteinbach/WeConnect-cli/releases/latest)
[![GitHub](https://img.shields.io/github/license/tillsteinbach/WeConnect-cli)](https://github.com/tillsteinbach/WeConnect-cli/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/tillsteinbach/WeConnect-cli)](https://github.com/tillsteinbach/WeConnect-cli/issues)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/weconnect-cli?label=PyPI%20Downloads)](https://pypi.org/project/weconnect-cli/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/weconnect-cli)](https://pypi.org/project/weconnect-cli/)
[![Donate at PayPal](https://img.shields.io/badge/Donate-PayPal-2997d8)](https://www.paypal.com/donate?hosted_button_id=2BVFF5GJ9SXAJ)
[![Sponsor at Github](https://img.shields.io/badge/Sponsor-GitHub-28a745)](https://github.com/sponsors/tillsteinbach)

Commandline Interface to interact with the Volkswagen WeConnect Services

## What is the purpose?
If you want to query data from weconnect you can use this command line interface to query the service. This commandline interface behaves like a user using the WeConnect ID App and the WeConnect secion on myvolkswagen.de. Use this if you want to work with the data from WeConnect.

## Requirements
You need to install python 3 on your system: [How to install python](https://realpython.com/installing-python/)

## How to install
If you want to use WeConnect-cli, the easiest way is to obtain it from [PyPI](https://pypi.org/project/weconnect-cli/). Just install instead using:
```bash
pip3 install weconnect-cli
```
### Updates
If you want to update WeConnect-cli, the easiest way is:
```bash
pip3 install weconnect-cli --upgrade
```

## How to use
Start weconnect-cli from the commandline, by default you will enter the interactive shell:
```bash
weconnect-cli --username user@mail.de --password test123
```
You get all the usage information by using the --help command
```bash
weconnect-cli --help
```
With the "list" command you can get a list of all available information you can query (use "list -s" if you want to see which attributes can be changed)
```bash
weconnect-cli --username user@mail.de --password test123 list
/vehicles/WVWABCE1ZSD057394
/vehicles/WVWABCE1ZSD057394/vin
/vehicles/WVWABCE1ZSD057394/role
/vehicles/WVWABCE1ZSD057394/enrollmentStatus
/vehicles/WVWABCE1ZSD057394/model
/vehicles/WVWABCE1ZSD057394/nickname
/vehicles/WVWABCE1ZSD057394/capabilities
...
```
You can then pass the addresses to the "get" command:
```bash
weconnect-cli --username user@mail.de --password test123 get /vehicles/WVWABCE1ZSD057394/model
ID.3
```
or the "set" command:
```bash
weconnect-cli --username user@mail.de --password test123 set /vehicles/WVWABCE1ZSD057394/controls/climatization stop
```
The "events" command allows you to monitor what is happening on the WeConnect Interface:
```bash
weconnect-cli --username user@mail.de --password test123 events
2021-05-26 16:49:58.698570: /vehicles/WVWABCE1ZSD057394/status/accessStatus/overallStatus: new value: unsafe
2021-05-26 16:49:58.698751: /vehicles/WVWABCE1ZSD057394/status/accessStatus/doors/bonnet/lockState: new value: unknown lock state
2021-05-26 16:49:58.698800: /vehicles/WVWABCE1ZSD057394/status/accessStatus/doors/bonnet/openState: new value: closed
2021-05-26 16:49:58.698980: /vehicles/WVWABCE1ZSD057394/status/accessStatus/doors/frontLeft/lockState: new value: unlocked
2021-05-26 16:49:58.699056: /vehicles/WVWABCE1ZSD057394/status/accessStatus/doors/frontLeft/openState: new value: closed
```
### Interactive Shell
You can also use an interactive shell:
```
weconnect-cli --username user@mail.de --password test123 shell
Welcome! Type ? to list commands
user@mail.de@weconnect-sh:/$update
update done
user@mail.de@weconnect-sh:/$cd vehicles
user@mail.de@weconnect-sh:/vehicles$ ls
..
WVWABCE1ZSD057394
WVWABCE13SD057505
user@mail.de@weconnect-sh:/vehicles$ cd /vehicles/WVWABCE13SD057505/status/parkingPosition
user@mail.de@weconnect-sh:/vehicles/WVWABCE13SD057505/status/parkingPosition$ cat
[parkingPosition] (last captured 2021-06-01T19:05:04+00:00)
	Latitude: 51.674535
	Longitude: 16.154376
user@mail.de@weconnect-sh:/vehicles/WVWZZZ3CZME112096/status/parkingPosition$ exit
Bye
```
### Caching
By default weconnect-cli will cache (store) the data for 300 seconds before retrieving new data from the servers. This makes weconnect-cli more responsive and at the same time does not cause unneccessary requests to the vw servers. If you want to increase the cache duration use --interval option. If you do not want to cache use --no-cache option. Please use the no-cache option with care. You are generating traffic with subsequent requests.

### Credentials
If you do not want to provide your username or password all the time you have to create a ".netrc" file at the appropriate location (usually this is your home folder):
```
machine volkswagen.de
login test@test.de
password testpassword123
```
You can also provide the location of the netrc file using the --netrc option
## Tested with
- Volkswagen ID.3 Modelyear 2021
- Volkswagen Passat GTE Modelyear 2021

## Reporting Issues
Please feel free to open an issue at [GitHub Issue page](https://github.com/tillsteinbach/WeConnect-cli/issues) to report problems you found.

### Known Issues
- The Tool is in alpha state and may change unexpectedly at any time!

## Related Projects:
- [WeConnect-MQTT](https://github.com/tillsteinbach/WeConnect-mqtt): MQTT Client that publishes data from Volkswagen WeConnect
- [WeConnect-python](https://github.com/tillsteinbach/WeConnect-python): Python API to connect to Volkswagen WeConnect Services
