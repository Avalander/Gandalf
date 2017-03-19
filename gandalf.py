#!/usr/bin/python
import argparse
import os
import subprocess

commands = [
	'create',
	'run',
	'list'
]

_gandalf_dir = os.path.join(os.path.expanduser('~'), '.gandalf')

def create(name):
	gandalf_dir = _gandalf_dir
	script_file = os.path.join(gandalf_dir, name)
	if not os.path.exists(gandalf_dir):
		os.mkdir(gandalf_dir)
	if os.path.exists(script_file):
		raise Exception('Script \'' + name + '\' already exists.')
	open(script_file, 'a').close()
	return_code = subprocess.call(['nano', script_file])

def run(name):
	script_file = os.path.join(os.path.expanduser('~'), '.gandalf', name)
	if not os.path.exists(script_file):
		raise Exception('Script \'' + name + '\' doesn\'t exist.')
	print('* Running script \'{}\' *\n'.format(name))
	result = subprocess.check_call(['/bin/bash', script_file])
	print('\n* Execution finished *\n')

def _list(name):
	subprocess.check_call(['ls', '-l', _gandalf_dir])
	pass

command_handlers = {
	'create': create,
	'list': _list,
	'run': run
}

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('command', metavar='C', help='Command to execute', choices=commands)
	parser.add_argument('name', help='Name of the script to create')
	args = parser.parse_args()
	command_handlers[args.command](args.name)

if __name__ == '__main__':
	main()
