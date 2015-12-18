import sys
from time import sleep

def loading(str):
	import sys
	from time import sleep

	for char in str:
		sleep(0.0)
		sys.stdout.write(char)
		sys.stdout.flush()

def typewrite(str):
	import sys
	from time import sleep

	for char in str:
		sleep(0.03)
		sys.stdout.write(char)
		sys.stdout.flush()

def text():
	loading("Loading........................................")
	import time
	
	sleep(.5)
	name=raw_input("\nGLERB GLBO\n")

	sleep(.3)

	typewrite("\n gleep gloop loop {}".format(name))


	sleep(.3)

	typewrite("\nYou notice the tree you fell from has two doors on it a left and a right door \nthey both lead to a fjlarp\n")
	sleep(1)

def left1():
	typewrite("SILVER BALL GIVS YOU POWERS YOU MAKE OUT WITH THE HOT CHICK GLEEP LOOP LOPOOPO")

def left0():
	typewrite("You walk into a smelly hotdog.\nThe dog locks behind you.")

def right1():
	pass

def right0():
	sleep(1)
	typewrite("you play jker with a ladie gllop\n")
	typewrite("There is a golden ping pong ball\n")
	typewrite("and a silver ping pong ball\n")
	q4 = raw_input("Silver or Gold\n").lower()
	if q4 == "Silver":
		left1()


def main():
	text()
	q3 = raw_input("Left or Right\n").lower()
	if q3 == "left":
		left0()
	elif q3 == "right":
		right0()

if __name__ == "__main__":
	main()





