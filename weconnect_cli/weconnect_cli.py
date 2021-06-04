from datetime import datetime
import sys
import os
import argparse
import netrc
import getpass
import logging
import time
import tempfile
import cmd
from enum import Enum

from weconnect import weconnect, addressable, errors

from .__version import __version__

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
DEFAULT_LOG_LEVEL = "ERROR"

LOG = logging.getLogger("weconnect-cli")


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


def main():  # noqa: C901 # pylint: disable=too-many-statements,too-many-branches,too-many-locals
    parser = argparse.ArgumentParser(
        prog='weconnect-cli',
        description='Commandline Interface to interact with the Volkswagen WeConnect Services')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('-u', '--username', help='Username of Volkswagen id', required=False)
    parser.add_argument('-p', '--password', help='Password of Volkswagen id', required=False)
    defaultNetRc = os.path.join(os.path.expanduser("~"), ".netrc")
    parser.add_argument('--netrc', help=f'File in netrc syntax providing login (default: {defaultNetRc}).'
                        ' Netrc is only used when username and password are not provided  as arguments',
                        default=None, required=False)
    parser.add_argument('-v', '--verbose', action="append_const", const=-1,)
    parser.add_argument('--no-token-storage', dest='noTokenStorage', help='Do not store token on filesystem (this'
                        ' will cause a new login for every invokation!)', action='store_true')
    defaultTemp = os.path.join(tempfile.gettempdir(), 'weconnect.token')
    parser.add_argument('--tokenfile', help=f'file to store token (default: {defaultTemp})', default=defaultTemp)
    parser.add_argument('--no-cache', dest='noCache', help='Do not use cache', action='store_true')
    defaultCacheTemp = os.path.join(tempfile.gettempdir(), 'weconnect.cache')
    parser.add_argument('--cachefile', help=f'file to store cache (default: {defaultCacheTemp})',
                        default=defaultCacheTemp)
    parser.add_argument('-i', '--interval', help='Query interval in seconds, used for cache and events',
                              type=NumberRangeArgument(1), required=False, default=300)

    parser.set_defaults(command='shell')

    subparsers = parser.add_subparsers(title='commands', description='Valid commands',
                                       help='The following commands can be used')
    parserList = subparsers.add_parser('list', aliases=['l'], help='List available ressource ids and exit')
    parserList.add_argument('-s', '--setters', help='List attributes that can be set', action='store_true')
    parserList.set_defaults(command='list')
    parserGet = subparsers.add_parser('get', aliases=['g'], help='Get ressources by id and exit')
    parserGet.add_argument('id', metavar='ID', type=str, help='Id to fetch')
    parserGet.set_defaults(command='get')
    parserGet = subparsers.add_parser('set', aliases=['s'], help='Set ressources by id and exit')
    parserGet.add_argument('id', metavar='ID', type=str, help='Id to set')
    parserGet.add_argument('value', metavar='VALUE', type=str, help='Value to set')
    parserGet.set_defaults(command='set')
    parserEvents = subparsers.add_parser(
        'events', aliases=['e'], help='Continously retrieve events and show on console')
    parserEvents.set_defaults(command='events')
    parserShell = subparsers.add_parser(
        'shell', aliases=['sh'], help='Start WeConnect shell')
    parserShell.set_defaults(command='shell')

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
        if args.netrc is not None:
            netRcFilename = args.netrc
        else:
            netRcFilename = defaultNetRc
        try:
            secrets = netrc.netrc(file=args.netrc)
            username, _, password = secrets.authenticators("volkswagen.de")
        except TypeError:
            if not args.username:
                LOG.error('volkswagen.de entry was not found in %s netrc-file. Create it or provide at least a username'
                          ' with --username', netRcFilename)
                sys.exit(1)
            username = args.username
            password = getpass.getpass()
        except FileNotFoundError:
            if not args.username:
                LOG.error('%s netrc-file was not found. Create it or provide at least a username with --username',
                          netRcFilename)
                sys.exit(1)
            username = args.username
            password = getpass.getpass()
    tokenfile = None
    if not args.noTokenStorage:
        tokenfile = args.tokenfile

    try:  # pylint: disable=too-many-nested-blocks
        weConnect = weconnect.WeConnect(username=username, password=password, tokenfile=tokenfile,
                                        updateAfterLogin=False, loginOnInit=False)
        if args.noCache or not os.path.isfile(args.cachefile):
            weConnect.login()
        else:
            weConnect.fillCacheFromJson(args.cachefile, maxAge=args.interval)

        if args.command == 'shell':
            try:
                weConnect.update()
                # disable caching
                weConnect.clearCache(maxAge=None)
                WeConnectShell(weConnect).cmdloop()
            except KeyboardInterrupt:
                pass
        elif args.command == 'list':
            weConnect.update()
            allElements = weConnect.getLeafChildren()
            for element in allElements:
                if args.setters:
                    if isinstance(element, addressable.ChangeableAttribute):
                        print(element.getGlobalAddress())
                else:
                    print(element.getGlobalAddress())
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
                sys.exit(-1)
        elif args.command == 'set':
            weConnect.update()
            element = weConnect.getByAddressString(args.id)
            if element:
                try:
                    if element.valueType in [int, float]:
                        newValue = element.valueType(args.value)
                    elif issubclass(element.valueType, Enum):
                        newValue = element.valueType(args.value)
                        try:
                            allowedValues = element.valueType.allowedValues()
                            if newValue not in allowedValues:
                                raise ValueError('Value is not in allowed values')
                        except AttributeError:
                            pass
                        newValue = element.valueType(args.value)
                    else:
                        newValue = args.value
                    if newValue == element.value:
                        print(f'id {args.id} cannot be set. Value {args.value} is already set', file=sys.stderr)
                        sys.exit(-1)
                    element.value = newValue
                except ValueError:
                    valueFormat = ''
                    if element.valueType == int:
                        valueFormat = 'N (Decimal number)'
                    elif element.valueType == float:
                        valueFormat = 'F.F (Floating Point Number)'
                    elif element.valueType == bool:
                        valueFormat = 'True/False (Boolean)'
                    elif issubclass(element.valueType, Enum):
                        try:
                            valueFormat = 'select one of [' + ', '.join([enum.value for enum in element.valueType.allowedValues()]) + ']'
                        except AttributeError:
                            valueFormat = 'select one of [' + ', '.join([enum.value for enum in element.valueType])
                    print(f'id {args.id} cannot be set. You need to provide it in the correct format {valueFormat}',
                          file=sys.stderr)
                    sys.exit(-1)
                except NotImplementedError:
                    print(f'id {args.id} cannot be set. You can see all changeable entries with "list -s"',
                          file=sys.stderr)
                    sys.exit(-1)
                except errors.SetterError as err:
                    print(f'id {args.id} cannot be set: %s', err, file=sys.stderr)
                    sys.exit(-1)
            else:
                print(f'id {args.id} not found', file=sys.stderr)
                sys.exit(-1)
        elif args.command == 'events':
            if args.noCache:
                LOG.warning('ignoring --no-cache parameter in events mode')

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

            weConnect.addObserver(observer, addressable.AddressableLeaf.ObserverEvent.VALUE_CHANGED,
                                  priority=addressable.AddressableLeaf.ObserverPriority.USER_MID)
            while True:
                weConnect.update()
                time.sleep(args.interval)
        else:
            LOG.error('command not implemented')
            sys.exit(-1)
        if not args.noTokenStorage:
            weConnect.persistTokens()
        if not args.noCache:
            weConnect.persistCacheAsJson(args.cachefile)
    except errors.AuthentificationError as e:
        LOG.critical('There was a problem when authenticating with WeConnect: %s', e)
        sys.exit(-1)
    except errors.APICompatibilityError as e:
        LOG.critical('There was a problem when communicating with WeConnect.'
                     ' If this problem persists please open a bug report: %s', e)
        sys.exit(-1)


class WeConnectShell(cmd.Cmd):
    prompt = 'error'
    intro = "Welcome! Type ? to list commands"

    def __init__(self, weConnect, completekey='tab', stdin=None, stdout=None,):
        self.weconnect = weConnect
        self.pwd = weConnect
        super().__init__(completekey=completekey, stdin=stdin, stdout=stdout)
        self.setPrompt(self.weconnect.getGlobalAddress())

    def setPrompt(self, path):
        if path == '':
            path = '/'
        WeConnectShell.prompt = f'{self.weconnect.username}@weconnect-sh:{path}$'

    def help_exit(self):  # pylint: disable=no-self-use
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_exit(self, arguments):  # pylint: disable=no-self-use
        del arguments
        print("Bye")
        return True

    def help_cd(self):  # pylint: disable=no-self-use
        print('change location in tree')

    def do_cd(self, arguments):
        if arguments is None or arguments == '':
            arguments = '/'
        if arguments.startswith('/'):
            path = arguments
        else:
            path = f'{self.pwd.getGlobalAddress()}/{arguments}'
        newPwd = self.weconnect.getByAddressString(path)
        if newPwd is not None and newPwd:
            self.pwd = newPwd
            path = self.pwd.getGlobalAddress()
            if path == '':
                path = '/'
            self.setPrompt(path)
        else:
            print(f'*** {arguments} does not exist')

    def complete_cd(self, text, line, begidx, endidx):
        del line
        del begidx
        del endidx
        if text.startswith('/'):
            return [child.getGlobalAddress() for child in self.weconnect.getLeafChildren() if child.getGlobalAddress().startswith(text)]
        return [child.getLocalAddress() for child in self.pwd.children if child.getLocalAddress().startswith(text)]

    def help_ls(self):  # pylint: disable=no-self-use
        print('list subelements of current path')

    def do_ls(self, arguments):
        del arguments
        if self.pwd.parent is not None:
            print('..')
        if isinstance(self.pwd, addressable.AddressableObject):
            for child in self.pwd.children:
                print(child.getLocalAddress())

    def help_pwd(self):  # pylint: disable=no-self-use
        print('show current path')

    def do_pwd(self, arguments):
        del arguments
        path = self.pwd.getGlobalAddress()
        if path == '':
            path = '/'
        print(path)

    def help_update(self):  # pylint: disable=no-self-use
        print('update the data from the server')

    def do_update(self, arguments):
        del arguments
        self.weconnect.update()
        print('update done')

    def help_cat(self):  # pylint: disable=no-self-use
        print('Print content')

    def do_cat(self, arguments):
        del arguments
        print(str(self.pwd))

    def help_find(self):  # pylint: disable=no-self-use
        print('Find lists all elements recursively')

    def do_find(self, arguments):
        setters = bool(arguments == '-s')
        allElements = self.pwd.getLeafChildren()
        for element in allElements:
            if setters:
                if isinstance(element, addressable.ChangeableAttribute):
                    print(element.getGlobalAddress())
            else:
                print(element.getGlobalAddress())

    def default(self, line):
        if line in ('x', 'q'):
            return self.do_exit(line)
        return super().default(line)

    do_EOF = do_exit
    help_EOF = help_exit
