class styles:
	green = '\033[92m'
	red = '\033[91m'
	blue = '\033[94m'
	bold = '\033[1m'
	warning = '\033[93m'
	underline = '\033[4m'
	end = '\033[0m'


def colour_text(text, *args):
	style = ''.join(*args)
	return '{}{}{}'.format(style, text, styles.end)


def cprint(*args):
	result = []
	for arg in args:
		if isinstance(arg, tuple):
			result.append(colour_text(arg[0], arg[1:]))
		else:
			result.append(arg)
	print(' '.join(result))
