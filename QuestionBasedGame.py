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

name=raw_input("What Is Your Name?\n")

def text():
	typewrite ("\nThis is a text based game")
	typewrite ("\nThis is a trial game and not finished")
	sleep(.5)
	typewrite ("\n{} You see two villages ahead one on the left or on the right".format(name))

def left0():
	typewrite ("\nYou walk to the village on the left\n you notice its quite clean and niffty")
	typewrite ("\n You see a pub and a general market")
	q2 = raw_input("\n Pub or Market\n").lower()
	if q2 == "pub":
		pub()
	elif q2 == "market":
		market()
		
		
		
def right0():
	typewrite ("\n You Sprint towrds this village becuase this is not a village you have ever seen before its extra unordianry\n")
	typewrite ("\n You see people Flying Zipping around on mechanical lines you see elvavotors that go higher than ever before\n")
	typewrite ("\n what will you do You see somone standing there with a sign on information to this new town or will you just go to the evlavtor and see where you go\n")
	q3 = raw_input("\n Talk or Explore").lower()
	if q3 == "talk":
		talk()
	elif q3 == "explore":
		explore()

def main():
	text()
	q1 = raw_input("\nplease choose the village you want to enter\nLeft or Right\n").lower()
	if q1 == "left":
		left0()
	elif q1 == "right":
		right0()

if __name__ == "__main__":
	main()
