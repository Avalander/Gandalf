import os
import subprocess

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
	print(os.listdir(_gandalf_dir))


def remove(name):
	script_file = os.path.join(_gandalf_dir, name)
	try:
		os.remove(script_file)
	except OSError:
		if os.path.exists(script_file):
			print('Could not remove script \'{}\''.format(script_file))


handlers = {
	'create': create,
	'list': _list,
	'run': run,
	'remove': remove
}
