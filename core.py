from components import *

def error_handle(args, arg_len):
	errors = {
	'add': 'Missing tasks string. Nothing added!',
	'done': 'Missing NUMBER for marking tasks as done.',
	'del': 'Missing NUMBER for deleting tasks.',
	}

	if args[0] == 'add' and arg_len != 3:
		error(errors[args[0]]) 
	if args[0] == 'done' and arg_len != 2:
		error(errors[args[0]]) 
	if args[0] == 'del' and arg_len != 2:
		error(errors[args[0]]) 


def core(args, arg_len):

	#when no argument is given
	if arg_len == 0:
		help()
		exit()

	if arg_len > 3:
		error()

	#when one or more argumenet is given
	else:
		args[0] = args[0].lower()
		error_handle(args, arg_len)

		if args[0] == 'help':
			help()


		elif args[0] == 'ls':
			list()


		elif args[0] == 'report':
			report()

		elif args[0] == 'reset':
			reset()

		elif args[0] == 'del':
			if args[1].isnumeric(): 
				delete(int(args[1]))
			else: 
				error()


		elif args[0] == 'done':
			if args[1].isnumeric(): 
				done(int(args[1]))
			else: 
				error("provide a number")


		elif args[0] == 'add':
			if args[1].isnumeric(): 
				add(int(args[1]), args[2])	
			else: 
				error()

		else:
			error()

	return