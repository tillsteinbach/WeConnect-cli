from datetime import datetime
import sys
import os
import argparse
import netrc
import getpass
import logging
import time
import tempfile

from weconnect import weconnect, addressable

from .__version import __version__

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
DEFAULT_LOG_LEVEL = "ERROR"


class NumberRangeArgument:

    def __init__(self, imin=None, imax=None):
        self.imin = imin
        self.imax = imax

    def __call__(self, arg):
        try:
            value = int(arg)
        except ValueError as e:
            raise self.exception() from e
        if (self.imin is not None and value < self.imin) or (self.imax is not None and value > self.imax):
            raise self.exception()
        return value

    def exception(self):
        if self.imin is not None and self.imax is not None:
            return argparse.ArgumentTypeError(f'Must be a number from {self.imin} to {self.imax}')
        if self.imin is not None:
            return argparse.ArgumentTypeError(f'Must be a number not smaller than {self.imin}')
        if self.imax is not None:
            return argparse.ArgumentTypeError(f'Must be number not larger than {self.imax}')

        return argparse.ArgumentTypeError('Must be a number')


def main():  # noqa: C901
    parser = argparse.ArgumentParser(
        prog='weconnect-cli',
        description='Commandline Interface to interact with the Volkswagen WeConnect Services')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('-u', '--username', help='Username of Volkswagen id', required=False)
    parser.add_argument('-p', '--password', help='Password of Volkswagen id', required=False)
    parser.add_argument('--netrc', help='File in netrc syntax providing login, default is the default netrc location '
                        '(usually your users folder). Netrc is only used when username and password are not provided '
                        'as arguments', default=None, required=False)
    parser.add_argument('-v', '--verbose', action="append_const", const=-1,)
    parser.add_argument('--no-token-storage', dest='noTokenStorage', help='Do not store token on filesystem (this'
                        ' will cause a new login for every invokation!)', action='store_true')
    defaultTemp = os.path.join(tempfile.gettempdir(), 'weconnect.token')
    parser.add_argument('--tokenfile', help=f'file to store token (default: {defaultTemp})', default=defaultTemp)
    parser.add_argument('--cache', help='Write http requests to cache and use those in subsequent calls when'
                        ' --fromcache was provided', action='store_true')
    parser.add_argument('--fromcache', help='Use previously captured data stored with --cache', action='store_true')
    defaultCacheTemp = os.path.join(tempfile.gettempdir(), 'weconnect.cache')
    parser.add_argument('--cachefile', help=f'file to store cache (default: {defaultTemp})', default=defaultCacheTemp)

    parser.set_defaults(command='none')

    subparsers = parser.add_subparsers(title='commands', description='Valid commands',
                                       help='The following commands can be used')
    parserList = subparsers.add_parser('list', aliases=['l'], help='List available ressource ids and exit')
    parserList.set_defaults(command='list')
    parserGet = subparsers.add_parser('get', aliases=['g'], help='Get ressources by id and exit')
    parserGet.add_argument('id', metavar='ID', type=str, help='Id to fetch')
    parserGet.set_defaults(command='get')
    parserEvents = subparsers.add_parser(
        'events', aliases=['e'], help='Continously retrieve events and show on console')
    parserEvents.set_defaults(command='events')
    parserEvents.add_argument('-i', '--interval', help='Query interval in seconds',
                              type=NumberRangeArgument(1), required=False, default=300)

    args = parser.parse_args()
    logLevel = LOG_LEVELS.index(DEFAULT_LOG_LEVEL)
    for adjustment in args.verbose or ():
        logLevel = min(len(LOG_LEVELS) - 1, max(logLevel + adjustment, 0))

    logging.basicConfig(level=LOG_LEVELS[logLevel])

    username = None
    password = None

    if args.username is not None and args.password is not None:
        username = args.username
        password = args.password
    else:
        try:
            secrets = netrc.netrc(file=args.netrc)
            username, _, password = secrets.authenticators("volkswagen.de")
        except FileNotFoundError:
            if not args.username:
                print('.netrc file was not found. Create it or provide at least a username with --username',
                      file=sys.stderr)
                sys.exit(1)
            username = args.username
            password = getpass.getpass()
    tokenfile = None
    if not args.noTokenStorage:
        tokenfile = args.tokenfile

    weConnect = weconnect.WeConnect(username=username, password=password, tokenfile=tokenfile, updateAfterLogin=False,
                                    loginOnInit=(not args.fromcache))
    if args.fromcache:
        weConnect.fillCacheFromJson(args.cachefile)

    if args.command == 'none':
        weConnect.update()
        print(weConnect)
    elif args.command == 'list':
        weConnect.update()
        allElements = weConnect.getLeafChildren()
        for element in allElements:
            print(element)
    elif args.command == 'get':
        weConnect.update()
        element = weConnect.getByAddressString(args.id)
        if element:
            if isinstance(element, dict):
                print('\n'.join([str(value) for value in element.values()]))
            else:
                print(element)
        else:
            print(f'id {args.id} not found', file=sys.stderr)
    elif args.command == 'events':
        def observer(element, flags):
            if flags & addressable.AddressableLeaf.ObserverEvent.ENABLED:
                print(str(datetime.now()) + ': ' + element.getGlobalAddress() + ': new object created')
            elif flags & addressable.AddressableLeaf.ObserverEvent.DISABLED:
                print(str(datetime.now()) + ': ' + element.getGlobalAddress() + ': object not available anymore')
            elif flags & addressable.AddressableLeaf.ObserverEvent.VALUE_CHANGED:
                print(str(datetime.now()) + ': ' + element.getGlobalAddress() + ': new value: ' + str(element))
            elif flags & addressable.AddressableLeaf.ObserverEvent.UPDATED_FROM_SERVER:
                print(str(datetime.now()) + ': ' + element.getGlobalAddress()
                      + ': was updated from server but did not change: ' + str(element))
            else:
                print(str(element.lastUpdateFromServer) + ' (' + str(flags) + '): '
                      + element.getGlobalAddress() + ': ' + str(element))

        weConnect.addObserver(observer, addressable.AddressableLeaf.ObserverEvent.VALUE_CHANGED)
        while True:
            weConnect.update()
            time.sleep(args.interval)
    else:
        print('command not implemented', file=sys.stderr)
    if not args.fromcache:
        weConnect.persistTokens()
    if args.cache:
        weConnect.persistCacheAsJson(args.cachefile)
