import sys
import shelve


from core import core


if __name__ == "__main__":
	
	args = sys.argv[1:]
	arg_len = len(args)

	core(args, arg_len)