import sys
import shelve

from core import core


if __name__ == "__main__":
	#get the arguments and store it in a variable
	args = sys.argv[1:]
	arg_len = len(args)

	core(args, arg_len)