import os
import shutil
import subprocess

from console import cprint, styles


_GANDALF_DIR = os.path.join(os.path.expanduser('~'), '.gandalf')
_TEMPLATES_DIR = os.path.join(_GANDALF_DIR, '.templates')


def add_template(path, editor='nano'):
	if os.path.exists(path):
		_add_files(path)
	else:
		_create_file(path, editor)


def remove(path):
	template_file = os.path.join(_TEMPLATES_DIR, path)
	try:
		os.remove(template_file)
		cprint(('Template \'{}\' removed successfully.'.format(path), styles.blue))
	except OSError as e:
		if os.path.exists(template_file):
			raise e


def _add_files(path):
	root_path = path.split('/')[-1]
	if len(root_path) == 0:
		root_path = path.split('/')[-2]
	shutil.copytree(path, os.path.join(_TEMPLATES_DIR, root_path))


def _create_file(path, editor):
	template_file = os.path.join(_TEMPLATES_DIR, path)
	if os.path.exists(template_file):
		raise Exception('Template \'{}\' already exists.'.format(path))
	folders = reduce(_folder_reducer, [x for x in path.split('/') if len(x) > 0][:-1], [])
	print(folders)
	for folder in folders:
		os.mkdir(folder)
	open(template_file, 'a').close()
	return subprocess.call([editor, template_file])


def _folder_reducer(folders_array, folder):
	if len(folders_array) == 0:
		folders_array.append(os.path.join(_TEMPLATES_DIR, folder))
		return folders_array
	folders_array.append('/'.join([folders_array[-1], folder]))
	return folders_array


_HANDLERS = {
	'add': add_template,
	'remove': remove
}


def handle(command, **kwargs):
	return _HANDLERS[command](**kwargs)
