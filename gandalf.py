#!/usr/bin/python
import argparse
import os
import subprocess

import commands


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('command', metavar='C', help='Command to execute')
	parser.add_argument('name', nargs='?', help='Name of the script to create')
	parser.add_argument('-e', '--editor', dest='editor')
	args = parser.parse_args()
	try:
		commands.handlers[args.command](args.name)
	except KeyError:
		commands.run(args.command)


if __name__ == '__main__':
	main()
