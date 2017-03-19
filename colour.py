class colours:
	green = '\033[92m'
	red = '\033[91m'
	end = '\033[0m'
	blue = '\033[94m'
	bold = '\033[1m'
	WARNING = '\033[93m'
	UNDERLINE = '\033[4m'


def colour_text(text, colour):
	return '{}{}{}'.format(colour, text, colours.end)


def cprint(text, colour):
	print(colour_text(text, colour))
