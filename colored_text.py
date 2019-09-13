# colored_text.py
# A function that is called by all of the other programs that I'll be using.
# It allows me to print specific colored text to the console, for dialogue.
# Also a test to figure out how to make a module. Or library. Or whatever it's called.
# In order to use it correctly, you need to use a string of these print functions, swapping between white and whatever other color.
# Make sure variables are put in as print_<color>(str(<variable>))

# Importing the module that I'll be using for color. By default, it won't reset the color at the end of the line, so an exception has been made.
from time import sleep
from colorama import init, Fore
init(autoreset=True)


def print_red(text):
	for i in text:
			print(Fore.RED + str(i), end="")
			sleep(.02)
	print()

def print_green(text):
	for i in text:
		print(Fore.GREEN + str(i), end="")
		sleep(.02)
	print()

def print_yellow(text):
	print(Fore.YELLOW + str(text))

def print_blue(text):
	for i in text:
		print(Fore.BLUE + str(i), end="")
		sleep(.02)
	print()

def print_magenta(text):
	for i in text:
		print(Fore.MAGENTA + str(i), end="")
		sleep(.02)
	print()

def print_cyan(text):
	for i in text:
		print(Fore.CYAN + str(i), end="")
		sleep(.02)
	print()

def print_white(text):
	for i in text:
		print(Fore.WHITE + str(i), end="")
		sleep(.02)
	print()

def invalid():
	print_white(" That's an invalid action.\n")
	sleep(1)


# Testing to make sure all of the colors work in the console.
if __name__ == '__main__':
	print(Fore.RED +"Please don't break.", end="")
	sleep(1)
	print_red("Please don't break.")
	sleep(1)
	print(Fore.RED +"Please don't break.")
#	print_green("Did it work?\n")
#	print_yellow("Wait, really?!\n")
#	print_blue("God, I'm ecstatic.\n")
#	print_magenta("You have no idea how long I've worked on this.\n")
#	print_cyan("Now, to somehow make this a module.\n")
#	print_white("Back to work!\n")