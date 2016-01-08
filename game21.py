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
#from termcolor import colored 

def text():
	loading("Loading........................................")
	import time
	#print colored('hello this is my game enjoy m89', 'red')
	
	sleep(.5)
	name=raw_input("\nGLERB GLBO\n")
	if name == "kade":
		import sticks
	sleep(.3)

	typewrite("\n gleep gloop loop {}".format(name))


	sleep(.3)

	typewrite("\nYou notice the tree you fell from has two doors on it a left and a right door \nthey both lead to a fjlarp\n")
	sleep(1)

def blue1():
	typewrite("You join the blue team and they hand you a freaking hotdog...\n dont worry its a braught worst lfmao gg m8")
	typewrite("\nYou just stand there and have no idea whats going on buts thats ok\nThen sum Butt head runs at you with a hamster FIRMLy Griped in his hands\n looks like he is on memes \n the dank kind\n")

def red1():
	typewrite("you go into the red arean hoping to find team8s\nbut there is only hamsters\nyout think atleast\ndont forget you have been drugges m8 pirtay m9")
	typewrite("\nYou pick up your Pepe sword and grab a handfull of magic beans charlie\n Then You find a golden ticket\n YOU STARat TO SPRINT AT THIS BRO WHO LOOKS DUMB AND SMELLS LIKE CHEESE haha SOML lol!")

def bail1():
	typewrite("You leave Your HOT wife... DUMB BUMB WANTS GUM right get it ? no you don't\n frekign beta noob")
	typewrite("You Get lonley and go to a nice Park and sit down on a bench and read a book\n DO YOU WANT IT TO LOOP FOREVER?\n The Book is about how chicken noddle soup can improve your hp...")
	typewrite("\n")

def stay1():
	typewrite("\nYou and Your Hunnie Pop Go to coounsling and try to work tings out....\n but it gets so boring that you starting taking coaine to spice things up a little bit\n get it SPICE things up haha jk jk")

def left1():
	typewrite("The gold ball will make you able to eat allot of pizza and not got sick\nbruhhh You get into a ship")#next question i have to mentin that the ball is laced with lcd

def left0():
	typewrite("You walk into a smelly hotdog.\nThe dog locks behind you.")
	typewrite("You see some Lcd and you snort that meme\n")
	typewrite("SPoiler It turns out your in the hugner games and you got druged... BEata noob\n Blue OR RED TEAM??????")
	q6 = raw_input("\nBlue or Red\n").lower()
	if q6 == "blue":
		blue1()
	elif q6 == "red":
		red1()

def right1():
	typewrite("SILVER BALL GIVS YOU POWERS YOU marry  THE HOT CHICK GLEEP LOOP LOPOOPO")
	silver1()
	
def rightquestion1():
	q4 = raw_input("Silver or Gold\n").lower()
	if q4 == "silver":
		right1()
	elif q4 =="gold":
		left1()
	rightquestion1()

def right0():
	sleep(1)
	typewrite("you play jker with a ladie gllop\n")
	typewrite("There is a golden ping pong ball ")
	typewrite("and a silver ping pong ball\n")
	rightquestion1()
def silver1():
	typewrite("\n Ten YEARS LATER\n You and flearjk Are having RElationship Issuies That is a no goo my friend\n Will you try to Stay and Work it out OR BAIL\n")
	q5 = raw_input("Stay or Bail\n").lower()
	if q5 == "stay":
		stay1()
	elif q5 == "bail":
		bail1()

def main():
	text()
	q3 = raw_input("Left or Right\n").lower()
	if q3 == "left":
		left0()
	elif q3 == "right":
		right0()

if __name__ == "__main__":
	main()





