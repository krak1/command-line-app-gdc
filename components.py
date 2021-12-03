import shelve

def help():
	print("Usage:-")
	print("$ ./task add 2 \"hello world\" # Add a new item with priority 2 and text \"hello world\" to the list")
	print("$ ./task ls                  # Show incomplete priority list items sorted by priority in ascending order")
	print("$ ./task del INDEX           # Delete the incomplete item with the given index")
	print("$ ./task done INDEX          # Mark the incomplete item with the given index as complete")
	print("$ ./task help                # Show usage")
	print("$ ./task report              # Statistics")

def list():
	pass

def report():
	pass

def delete(num):
	pass

def done(num):
	pass

def add(priority, task):
	r = shelve.open('task.db')
	print(r['task'])


def error():
	pass