import argparse
import configparser

class Arguments():
    def __init__(self, args):
        args_dict = self._parse_arguments(args)

        if args_dict.p or args_dict.players:
            self.players = (args_dict.p or args_dict.players)[0].split(',')
        elif args_dict.f or args_dict.file:
            config = configparser.ConfigParser()
            config.read(args_dict.f or args_dict.file, encoding='utf-8')

            try:
                self.players = config['DEFAULT']['players'].split(',')
            except KeyError:
                raise Exception('set a config file that exists.')

    def _parse_arguments(self, args):
        parser = argparse.ArgumentParser()

        #defining arguments
        parser.add_argument('--players', nargs=1)
        parser.add_argument('-p', nargs=1)
        parser.add_argument('--file', nargs=1)
        parser.add_argument('-f', nargs=1)


        return parser.parse_args(args)
