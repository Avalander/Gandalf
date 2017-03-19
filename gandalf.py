#!/usr/bin/python
import argparse
import os
import subprocess

import commands


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('command', metavar='C', help='Command to execute')
	parser.add_argument('name', nargs='?', help='Name of the script to create')
	parser.add_argument('-e', '--editor', dest='editor', default=argparse.SUPPRESS)
	parser.add_argument('-d', '--description', dest='description', default=argparse.SUPPRESS)
	args = parser.parse_args()
	try:
		try:
			commands.handlers[args.command](**vars(args))
		except KeyError:
			commands.run(args.command)
	except Exception as e:
		print('\033[91m{}\033[0m'.format(e))


if __name__ == '__main__':
	main()
