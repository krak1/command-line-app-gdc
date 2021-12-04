import shelve

def help():
	print("Usage :-\n$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n$ ./task del INDEX            # Delete the incomplete item with the given index\n$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n$ ./task help                 # Show usage\n$ ./task report               # Statistics")
	# print("$ ./task reset               # Reset the list (delete all items and history)")
	exit()

	
def list():
	#opening the database using shelve moduel
	#All the tasks are stored under the key 'task'
	r = shelve.open('task.db')
	tasks_list = r['task'] 
	r.close()

	if len(tasks_list) == 0:
		print("There are no pending tasks!")
		exit()

	#iterating and printing the tasks
	for count, task_string in enumerate(tasks_list, 1):
		task = task_string[2:]
		priority = int(task_string[:2])
		print(str(count)+". "+task + " ["+str(priority)+"]")



def report():
	#getting list of tasks
	#opening the done list
	r = shelve.open('task.db')
	tasks_list = r['task']
	done_list = r['done']

	#getting the no. of tasks not done and done
	task_len = len(tasks_list)
	done_len = len(done_list)

	#printing the report
	
	print("Pending :", task_len)
	#iterating and printing the tasks_list
	for count, task_string in enumerate(tasks_list, 1):
		task = task_string[2:]
		priority = int(task_string[:2])
		print(str(count)+". "+task + " ["+str(priority)+"]")

	print("\nCompleted :", done_len)
	#iterating and printing the done_list
	for count, done_string in enumerate(done_list, 1):
		print(str(count)+". "+done_string)



def delete(num):

	#geting list from database
	r = shelve.open('task.db')
	tasks_list = r['task']
	#checking if the number is valid
	if len(tasks_list) < num or num <= 0:
		error("task with index #"+str(num)+" does not exist. Nothing deleted.")

	#removing the particular task
	tasks_list = tasks_list[:num-1]+tasks_list[num:]
	
	#updating the database under the specified key
	r['task'] = tasks_list
	r.close()

	print("Deleted task #"+ str(num))
	exit()


def done(num):

	#getting list of tasks
	r = shelve.open('task.db')
	tasks_list = r['task']
	
	#checking the validity of num
	if len(tasks_list) < num or num <= 0:
		error("no incomplete item with index #"+str(num)+" exists.")
	
	#all the completed items are stored in the database under the key 'done'
	#opening the done list
	done_list = r['done']

	#updating the done_list and task_list
	done_list.append(tasks_list[num-1][2:])
	tasks_list = tasks_list[:num-1]+tasks_list[num:]

	#updating the database
	r['task'] = tasks_list
	r['done'] = done_list
	r.close()

	print("Marked item as done.")


def add(priority, task):

	#getting the task_list
	r = shelve.open('task.db')
	tasks_list = r['task']
	done_list = r['done']

	#generating the task string
	#([PRIORITY][TASK]) this is how it is store in the database
	if priority < 10:
		task_string = "0" + str(priority) + task
	elif priority < 100:
		task_string = str(priority) + task
	else:
		error(" PRIORITY should be between 0-100 ")

	#adding the new task at the right position in the task_list
	if task_string not in tasks_list:
		added = False
		if task in done_list:
			done_list.remove(task)

		for i in range(len(tasks_list)):
			itr_task = tasks_list[i]

			if priority >= int(itr_task[:2]):
				continue
			else:
				tasks_list = tasks_list[0:i] + [task_string] + tasks_list[i:]
				added = True
				break;
		#if not added add at the last
		if not added:
			tasks_list.append(task_string)

	#updating the database
	r['task'] = tasks_list
	r['done'] = done_list
	r.close()

	print("Added task: \""+task+"\" with priority "+str(priority))


def reset():
	#deletes the lists under the given keys
	r = shelve.open('task.db')
	r['task'] = []
	r['done'] = []
	r.close()

	print("The list reset was successful")


def error(message=None):

	if message is not None:
		print("Error: " +message)
	else:
		print("Invalid !\n")
		help()
	#program will end when the error function is called
	exit()
