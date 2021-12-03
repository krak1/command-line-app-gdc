from components import *


def core(args, arg_len):

	#when no argument is given
	if arg_len == 0:
		help()

	#when one argumenet is given
	if arg_len == 1:
		if args[0].lower() == 'help':
			help()
		elif args[0].lower() == 'ls':
			list()
		elif args[0].lower() == 'report':
			report()
		else:
			error()

	#when two arguments are given
	if arg_len == 2:
		if args[0].lower() == 'del':
			if args[1].isnumeric(): delete(int(args[1]))
			else: error()
		elif args[0].lower() == 'done':
			if args[1].isnumeric(): done(int(args[1]))
			else: error()
		else:
			error()

	#when three arguments are given
	if arg_len == 3:
		if args[0].lower() == 'add':
			if args[1].isnumeric(): add(int(args[1]), args[2])	
			else: error()

	#when more than three arguments are given
	if arg_len > 3:
		error()

	return