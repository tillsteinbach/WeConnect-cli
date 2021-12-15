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

### Login & Consent
WeConnect-cli is based on the new WeConnect ID API that was introduced with the new series of ID cars. If you use another car or hybrid you probably need to agree to the terms and conditions of the WeConnect ID interface. Easiest to do so is by installing the WeConnect ID app on your smartphone and login there. If necessary you will be asked to agree to the terms and conditions.

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
### Charging Stations
To obtain data for charging stations you have to add a location to search for in geo coordinates and a search radius in meters:
```bash
weconnect-cli --chargingLocation 52.437132 10.796628 --chargingLocationRadius=500 get /chargingStations
ID:                  40a4b8d3-d534-422c-9cd8-81bbfa5b578f
Name:                VW Group Oebisfelder Straße Parkhaus Ost
Operator:            VW Group (Id: edd03be9-2df7-4fe3-be32-1573ba91aac0)
Latitude:            52.4370178
Longitude:           10.7977292
Distance:            76m
Address:             Oebisfelder Straße 1, 38448 Wolfsburg, Deutschland
Max. Charging Power: 50.0kW
Charging Spots: 2 items
	Availability: OCCUPIED
	Max. Charging Power: 22.0kW
	Connectors: 1 items
		Plug Type: Type2
		Max. Charging Power: 22.0kW

	Availability: AVAILABLE
	Max. Charging Power: 50.0kW
	Connectors: 1 items
		Plug Type: CCS
		Max. Charging Power: 50.0kW

Authentification:    RFID, APP, UNKNOWN, UNKNOWN
Options:             weCharge partner;
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
user@mail.de@weconnect-sh:/vehicles/WVWABCE13SD057505/status/parkingPosition$ exit
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

### Images
You can also work with images from the API
Either you have a look at the commandline
```
weconnect-cli get /vehicles/WVWABCE13SD057505/pictures/car
                                     zjo]?![[[[]!!??I*{{rlllcc?uzo7zjjuunT#Jwfy25Fmd
                                *JywJ##TTuua]1t7LLjLLLjz7ot[Ir]att11[[aaeeeeoooeozjzet[>
                             1T2p6p5Fmh4Jeut1eoeLT#nL1ou##jeLne]!]!1j[[][[[[[]]I}I][1tee?
                         =[nypmqgdXbbYgzaTuTfzI}}}I!t}jTwjjJL}llllc}Tz?I*}}*****ssr*}}I[1[l
                     rcsoCF6pmgddVhgg6aaCL1##1IIIIII}!ettTwt%%v%cr?]{eI{v%cccllrrrsr*I??aw!}
              Q@GEVgqTnw2yw##TTuuLjj7oaat[]!?IIIIII??!!!7nt{>="i%c{![oea[[taeeeeeeet1eeeetta]i
        a7uJCJ#nLjz7ot1]!?II}**{{srlllrs*}}}}}I?]1e7juLLLLzL1%}1[11teat!rI?I*{srlccvccls{{srri:
    ufzx%lrcv)<\)||"""""|||)\\<<>)%l{**{rs}[7u#TuLz77zjuTL7]I{lx%vi><<\)ii\\\\\\\\\<>>%rss*{cv"
  Ypje{cx%%%%%%v%xxxcccllrs{*?[ezLuTJwf36dGdFw6Vg#Ii\\)xlxi|///////////////////////++++;_'^\v)"
  Y&&F7t!I!?!?t1jt[[1ttttaju5hggV&DkgpdBDXSo}?ttr";:_..-^"|/==^^^^^^^^^;^;;;;;;;;;;;;^">i|__/\/
 #L#e]1*%v%ii\v<\>>ii%v%xclI1e1ajhZFuo#hS#[II*v/)l***c\,`:^^;;;;;;;;;;;;;^^^^==++/=,;/%s][c:;=^
33]||vrr***{*{{rxllrrrrrsrlrllrs{{{{***}I?}r%<"%r1}]ts]{\_;;;===++////""""""||||||/;^){s![!\"}r
]z}i:,:\EGPE6q6VE44d};^==^^=+/"|\ir*?!1tsc)|/=c1?*I]![[?{\,+""/////""|)\<>)vxcrs{***>)!?*}[%{oe
=/"\=^'^t77joo7nJwfyc_'::^+""|)\>%}????#a=""+/!I!*r1nIs!tv|<vxlr{*}I??!???}*{rlxv)<|^|]u{}7%?
>wt)=+^_-` `. .   . ._``://"/""|)\)ls{}!d{;\i%]!aos{e[*e7vl**{srlc%%vii))>><<\\/^;^^=/%1!oI"
 Ewz[><<<<<>)%{{srcv)v))vlrsrrrlll*e7zz7ei)I]{Ia71e{}IjT?)^;,:'_-`.              -^+///>xi/
   .g `:;==/\l[1[I%<)""""+///"||)|+====+="||/"v?l*e]]nf?|`                         `_:,'-
        `_''''':'_.                       -;+|\<vs*?Ic<^
                                            `:^^^=+=^:
```
but it makes more sense to save the image to a file: 
```bash
weconnect-cli save /vehicles/WVWABCE13SD057505/pictures/car car.png
ls -alh car.png
-rw-r--r--  1 tillsteinbach  staff   135K  5 Jul 15:07 car.png
```
If there is information regarding door, light and window status provided for your car you can also use the 'status' picture

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

## Seat, Cupra, Skoda IV, ...
In an effort to try to make WeConnect-cli also to work with latest generation of vehicles from other volkswagen brands I'm looking for users to temporarily share access to their accounts. If you are willing to support please send me a message.
- Already tried: Cupra Born (The API looks a bit different, maybe it is older, I will check again in some weeks), thanks to the user initdebugs
