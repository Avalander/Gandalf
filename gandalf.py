#!/usr/bin/python
import argparse

import commands
import console


class DefaultSubcommandArgParser(argparse.ArgumentParser):
	__default_subparser = None

	def set_default_subparser(self, name):
		self.__default_subparser = name

	def _parse_known_args(self, arg_strings, *args, **kwargs):
		in_args = set(arg_strings)
		d_sp = self.__default_subparser
		if d_sp is not None and not {'-h', '--help'}.intersection(in_args):
			for x in self._subparsers._actions:
				subparser_found = (
					isinstance(x, argparse._SubParsersAction) and
					in_args.intersection(x._name_parser_map.keys())
				)
				if subparser_found:
					break
			else:
				# insert default in first position, this implies no
				# global options without a sub_parsers specified
				arg_strings = [d_sp] + arg_strings
		return super(DefaultSubcommandArgParser, self)._parse_known_args(arg_strings, *args, **kwargs)


def parse_args():
	parser = DefaultSubcommandArgParser()
	subparsers = parser.add_subparsers(title='Commands', dest='command')

	# Create command
	create_parser = subparsers.add_parser('create', help='Creates a new script')
	create_parser.add_argument('name', help='Name of the script to create')
	create_parser.add_argument('-d', '--description', dest='description', default=argparse.SUPPRESS)
	create_parser.add_argument('-e', '--editor', dest='editor', default=argparse.SUPPRESS)

	# Edit command
	edit_parser = subparsers.add_parser('edit', help='Edits an existing script')
	edit_parser.add_argument('name', help='Name of the script to edit')
	edit_parser.add_argument('-e', '--editor', dest='editor', default=argparse.SUPPRESS)

	# List command
	list_parser = subparsers.add_parser('list', help='Lists all available scripts')

	# Remove command
	remove_parser = subparsers.add_parser('remove', help='Removes an existing script')
	remove_parser.add_argument('name', help='Name of the script to remove')

	# Run command
	run_parser = subparsers.add_parser('run', help='Executes an existing script')
	run_parser.add_argument('name', help='Name of the script to execute')
	run_parser.add_argument('-a', '--args', dest='script_args', nargs='*', default=argparse.SUPPRESS)

	# Template
	template_parser = subparsers.add_parser('template')
	template_parser.add_argument('template_command', choices=['add', 'edit', 'remove'])
	template_parser.add_argument('path')
	template_parser.add_argument('-e', '--editor', dest='editor', default=argparse.SUPPRESS)

	parser.set_default_subparser('run')

	return parser.parse_args()


def main():
	args = vars(parse_args())
	try:
		command = args.pop('command')
		commands.handle(command, **args)
	except Exception as e:
		console.cprint((e, console.styles.red))


if __name__ == '__main__':
	main()
