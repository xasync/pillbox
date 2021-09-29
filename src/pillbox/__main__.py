import os
import sys
import platform
import __version__ as v
import pillbox_support.conf as conf
import argparse

COMMAND_SERVER = 'server'
COMMAND_CONFIG = 'config'


def server_command(args):
    from pillbox import create_app
    if args.test:
        app = create_app()
        app.run(port=args.port, debug=True)
    else:
        from gevent import monkey, pywsgi
        monkey.patch_all()
        app = create_app()
        server = pywsgi.WSGIServer(('127.0.0.1', args.port), app)
        server.serve_forever()


def config_command(args):
    cfg = conf.Configure()
    if args.list:
        cfg.show()
        sys.exit()

    if args.name and not args.data:
        data = cfg.get(args.name)
        print data if data else '% is not config.' % (args.name)

    elif args.name and args.data:
        cfg.set(args.name, args.data)
    else:
        print 'unknown command syntax, execute pillbox config -h for help.'


def main():
    ap = argparse.ArgumentParser(prog=v.__title__, add_help=True, description=v.__description__)
    sub = ap.add_subparsers(dest='command', help='sub-command')
    sub_server = sub.add_parser(COMMAND_SERVER)
    sub_server.add_argument('-p', '--port', action='store', default=5000, help='port, or default 5000.')
    sub_server.add_argument('-t', '--test', action='store_true', default=False,
                            help='open the test mode,default false.')

    sub_config = sub.add_parser(COMMAND_CONFIG)
    sub_config.add_argument('-n', '--name', help='name,entry likes:name=data')
    sub_config.add_argument('-d', '--data', help='data,entry likes:name=data')
    sub_config.add_argument('-e', '--erase', help='erase entry')
    sub_config.add_argument('-l', '--list', required=False, action='store_true', help='show all config')

    ap.add_argument('-v', '--version', action='version', version=v.__version__, help='show version.')
    args = ap.parse_args()

    if args.command == COMMAND_SERVER:
        server_command(args)
    elif args.command == COMMAND_CONFIG:
        config_command(args)
    else:
        sys.exit('unknown command for pillbox!')


if __name__ == '__main__':
    main()
