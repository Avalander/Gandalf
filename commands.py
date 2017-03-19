from __future__ import print_function
import os
import subprocess

from colour import colour_text, styles

_description_header = '### DESCRIPTION: '
_gandalf_dir = os.path.join(os.path.expanduser('~'), '.gandalf')


def remove_command(f):
	def wrapper(command, **kwargs):
		return f(**kwargs) if len(kwargs) > 0 else f(command)
	return wrapper


@remove_command
def create(name, description=None):
	script_file = os.path.join(_gandalf_dir, name)
	if not os.path.exists(_gandalf_dir):
		os.mkdir(_gandalf_dir)
	if os.path.exists(script_file):
		raise Exception('Script \'{}\' already exists.'.format(name))
	with open(script_file, 'a') as f:
		if description:
			print('{}{}'.format(_description_header, description), file=f)
	return_code = subprocess.call(['nano', script_file])


@remove_command
def edit(name):
	script_file = os.path.join(_gandalf_dir, name)
	if not os.path.exists(script_file):
		raise Exception('Script \'{}\' doesn\'t exist'.format(name))
	subprocess.check_call(['nano', script_file])
	print(colour_text('Script \'{}\' updated successfully.'.format(name), styles.green))


@remove_command
def run(name):
	script_file = os.path.join(_gandalf_dir, name)
	if not os.path.exists(script_file):
		raise Exception('Script \'{}\' doesn\'t exist.'.format(name))
	print(colour_text('* Running script \'{}\' *\n'.format(name), styles.bold))
	result = subprocess.check_call(['/bin/bash', script_file])
	print(colour_text('\n* Execution finished *\n', styles.bold))


def get_file_description(filename):
	description = ''
	with open(filename, 'r') as f:
		desc_lines = [x.strip().replace(_description_header, '') for x in f.readlines() if x.startswith(_description_header)]
		description = ', '.join(desc_lines)
	return description


@remove_command
def _list(name):
	lines = []
	scripts = os.listdir(_gandalf_dir)
	max_length = reduce((lambda a, i: max(len(i), a)), scripts, 0)
	for script in scripts:
		desc = get_file_description(os.path.join(_gandalf_dir, script))
		lines.append('* {script}{spaces}{desc}'.format(**{
			'script': colour_text(script, styles.blue),
			'spaces': ' ' * (max_length - len(script) + 4),
			'desc': desc if desc else ''
		}))
	for line in lines:
		print(line)


@remove_command
def remove(name):
	script_file = os.path.join(_gandalf_dir, name)
	try:
		os.remove(script_file)
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
