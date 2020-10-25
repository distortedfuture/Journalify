import os
import random
from datetime import datetime
from shutil import rmtree

JOURNAL = os.getcwd() + "/journal/"

def main(*args):

	print("\n"*50)

	if args:
		for arg in args:
			print(arg)

	os.chdir(JOURNAL)
	
	print("welcome \n")
	print("what would you like to do?")
	print("1: create a new journal")
	print("2: open current journals")
	print("3: rename a journal")
	print("4: delete journal")
	print("5: delete all journals")
	print("6: get the fuck outta here")
	print("\n" *2) 

	try:
		choice = int(input("choose an option \n"))
	except ValueError as er:
		# print(er)
		main("Please type a number from the given options")

	if choice == 1:
		new_journal()

	elif choice == 2:
		open_journal()

	elif choice == 3:
		rename_journal()

	elif choice == 4:
		del_journal()
	
	elif choice == 5:
		del_all()

	elif choice == 6:
		print("Bye bitchhhhh")
		quit()

	else:
		main("please type a number from the given options")


def new_journal():
	print("\n"*3)


	# main_dir = os.getcwd()
	name = input("name your new journal \n")

	file_name = name.replace(" ", "-")

	try:
		os.mkdir(file_name)
	finally:
		print(f"created journal {name}")
		# print(os.listdir(main_dir+'/journal'))
		# main()
	author = input("enter your name: ")

	os.chdir(file_name)
	with open("author.txt", "w") as file:
		file.write("Author: " + author + "\n")

	# if input("1 to add an entry, 2 to go back \n")

	main()


def new_entry():
	print("\n"*10)

	name = input("name of entry: ")
	file_name = name.lower().replace(" ", "-") + ".txt"

	content = input("begin typing \n")

	date_obj = datetime.now()
	date = f"{date_obj.day}: {date_obj.month}: {date_obj.year}"

	with open("author.txt", "r") as a:
		author = a.read()

	with open(file_name, 'w') as file:

		file.write(author)
		file.write("\n")

		file.write(f"Date: {date}")
		file.write("\n")

		count = 0
		previous = 0

		for i in range(len(content) -1):
			if content[i] == " " or i == len(content) -1:
				count += 1
				file.write(content[previous:i])
				previous = i
			if count == 10:
				file.write("\n")
				count = 0
			# if i == len(content) - 1:
			# 	file.write(content[previous:i])


	print(f"added entry: {name}")
	main()


def open_journal():
	print("\n"*10)

	os.chdir(JOURNAL)

	dir_list = [item for item in os.listdir(os.getcwd()) if os.path.isdir(item)]

	if len(dir_list) > 0:
		for index, item in enumerate(dir_list):
			print(index, item)
	else:
		main("no journals to open")

	try:
		choice = int(input("which journal to open \n"))
	except ValueError as er:
		main(er)

	try:
		folder = dir_list[choice]
	except IndexError as er:
		main(er)

	os.chdir(folder)

	count = len(os.listdir())

	print(f"Currently showing: {folder}")
	print(f"current entries open: {count}" + '\n')

	print("*" * 30)
	print("choose an option")
	print("1: read an entry")
	print("2: add an entry")
	print("3: rename an entry")
	print("4: delete an entry")

	choice = input("select: ")

	if choice == "1":
		open_entry()

	elif choice == "2":
		new_entry()

	elif choice == "3":
		rename_entry()

	elif choice == "4":
		del_entry()

	else:
		main("yeah try selecting a valid option maybe")


def open_entry():
	print("\n"*3)

	entry_list = [f for f in os.listdir()]

	if len(entry_list) > 0:
		print(f" current entries: {len(entry_list)} \n")
		for index, item in enumerate(entry_list):
			print(index, ":", item)
	else:
		main("no entries to open")

	try:
		file = int(input("entry to read \n"))
	except ValueError as er:
		main(er)

	try:
		file = entry_list[file]
	except IndexError as er:
		main(er)

	with open(file, "r") as file:
		x = file.read()
		print(x)

	if input("Press any key to go back \n"):
		main()


def del_entry():
	print("\n"*10)
	
	entry_list = [f for f in os.listdir()]

	if len(entry_list) > 0:
		for index, name in enumerate(entry_list):
			print(index, ":", name)
	else:
		main("no entries to delete")

	try:
		choice = int(input("choose entry to delete\n"))
	except ValueError as er:
		main()

	try:
		entry = entry_list[choice]
	except IndexError as er:
		main("You did not select a valid option")

	if entry != "author.txt":
		os.remove(entry)
		main(f"removed entry {entry}")
	else:
		main("cannot remove this file bruh")

	main()


def del_journal():
	print("\n"*10)

	dir_list = [f for f in os.listdir() if os.path.isdir(f)]

	for index, item in enumerate(dir_list):
		print(index, ":", item)

	try:
		choice = int(input("Which journal to delete \n"))
	except ValueError:
		del_journal()

	try:
		choice = dir_list[choice]
	except IndexError as er:
		main("did not choose a valid option")

	if input(f"enter 1 to delete {choice}, press any key to cancel") == '1':
		rmtree(choice)
	else:
		main(f"{choice} was not deleted from memory")


def del_all():
	print("\n"*10)

	dir_list = [f for f in os.listdir() if os.path.isdir(f)]
	entry_list_arr = [os.listdir(d) for d in dir_list]

	print("\n"*2)
	print("the following entries will be erased from memory")
	print("\n")
	for d in dir_list:
		print(f"journal: {d}")
	for i in entry_list_arr:
		for j in i:
			print(j)

	confirm = int(input("type 1 to continue, 2 to go back \n"))

	if confirm == 1:
		for d in dir_list:
			print(f"Erasing {d} from memory...")
			rmtree(d)
		main()
	else:
		main()


def rename_journal():
	
	dir_list = [f for f in os.listdir() if os.path.isdir(f)]

	if len(dir_list) > 0:
		for index, name in enumerate(dir_list):
			print(index, ":", name)
	else:
		main("no journals to rename")

	try:
		choice = int(input("select a journal to rename \n"))
	except ValueError:
		rename_journal()

	try:
		choice = dir_list[choice]
	except IndexError as er:
		# print(er)
		main(er)

	new_name = input("new name: ").lower().replace(" ", '-')

	if input(f"Journal: {choice} will be renamed {new_name}, 1 if thats cool, 2 to refuse") == '1':
		os.rename(choice, new_name)
		main(f"{choice} has been renamed to {new_name}")
	else:
		main(f"{choice} has not been renamed")


def rename_entry():
	print("\n"*3)

	entry_list = [f for f in os.listdir()]

	for index, item in enumerate(entry_list):
		print(index, ":", item)

	try:
		choice = int(input("select entry to rename \n"))
	except ValueError:
		rename_entry()

	choice = entry_list[choice]

	new_name = input("New name \n").lower().replace(' ', '-') + ".txt"

	confirm = input(f"will rename {choice} to {new_name} \n type 1 to proceed, anything to go back")

	if confirm == "1":
		os.rename(choice, new_name)
		main()
	else:
		main()

if __name__ == "__main__":
	main("time to write")