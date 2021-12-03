from components import *


def core(args, arg_len):

	if arg_len == 0:
		help()

	if arg_len == 1:
		if args[0].lower() == 'help':
			help()
		elif args[0].lower() == 'ls':
			list()
		elif args[0].lower() == 'report':
			report()
		else:
			error()

	if arg_len == 2:
		if args[0].lower() == 'del':
			if args[0].isnumeric: delete(int(args[1]))
			else: error()
		elif args[0].lower() == 'done':
			if args[0].isnumeric: done(int(args[1]))
			else: error()

	if arg_len == 3:
		if args[0].lower() == 'add':
			if args[0].isnumeric: add(int(args[1]), args[2])
			else: error()

	if arg_len > 3:
		error()

	return 0