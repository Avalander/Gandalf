from __future__ import print_function
import os
import subprocess

from console import colour_text, styles

_DESCRIPTION_HEADER = '### DESCRIPTION: '
_GANDALF_DIR = os.path.join(os.path.expanduser('~'), '.gandalf')


def create(name, description=None, editor='nano'):
	script_file = os.path.join(_GANDALF_DIR, name)
	if not os.path.exists(_GANDALF_DIR):
		os.mkdir(_GANDALF_DIR)
	if os.path.exists(script_file):
		raise Exception('Script \'{}\' already exists.'.format(name))
	with open(script_file, 'a') as f:
		if description:
			print('{}{}'.format(_DESCRIPTION_HEADER, description), file=f)
	return subprocess.call([editor, script_file])


def edit(name, editor='nano'):
	script_file = os.path.join(_GANDALF_DIR, name)
	if not os.path.exists(script_file):
		raise Exception('Script \'{}\' doesn\'t exist'.format(name))
	subprocess.check_call([editor, script_file])
	print(colour_text('Script \'{}\' updated successfully.'.format(name), styles.green))


def run(name, script_args=None):
	script_file = os.path.join(_GANDALF_DIR, name)
	if not os.path.exists(script_file):
		raise Exception('Script \'{}\' doesn\'t exist.'.format(name))
	if script_args is None:
		script_args = []
	print(colour_text('* Running script \'{}\' *\n'.format(name), styles.bold))
	subprocess.check_call(['/bin/bash', script_file] + script_args)
	print(colour_text('\n* Execution finished *\n', styles.bold))


def _get_file_description(filename):
	description = ''
	with open(filename, 'r') as f:
		desc_lines = [x.strip().replace(_DESCRIPTION_HEADER, '')
			for x in f.readlines() if x.startswith(_DESCRIPTION_HEADER)]
		description = ', '.join(desc_lines)
	return description


def _list():
	lines = []
	scripts = os.listdir(_GANDALF_DIR)
	max_length = reduce((lambda a, i: max(len(i), a)), scripts, 0)
	for script in scripts:
		desc = _get_file_description(os.path.join(_GANDALF_DIR, script))
		lines.append('* {script}{spaces}{desc}'.format(
			script=colour_text(script, styles.blue),
			spaces=' ' * (max_length - len(script) + 4),
			desc=desc if desc else ''
		))
	for line in lines:
		print(line)


def remove(name):
	script_file = os.path.join(_GANDALF_DIR, name)
	try:
		os.remove(script_file)
		print(colour_text('Script \'{}\' removed successfully.'.format(name), styles.blue))
	except OSError as e:
		if os.path.exists(script_file):
			raise e


handlers = {
	'create': create,
	'edit': edit,
	'list': _list,
	'run': run,
	'remove': remove
}
