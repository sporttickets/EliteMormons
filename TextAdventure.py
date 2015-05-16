import sys
from time import sleep

def loading(str):
    import sys
    from time import sleep

    for char in str:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

def typewrite(str):
    import sys
    from time import sleep

    for char in str:
        sleep(0.0)
        sys.stdout.write(char)
        sys.stdout.flush()


    loading("Loading........................................")
    import time
    typewrite("\nNARRATOR:\nYou just woke up and you don't know where you are or your name...")

    time.sleep(3)

    typewrite("\nFredrick:\nAre you alright you just fell from that tree ...\n")

    time.sleep(2)

    typewrite("Whats your name?")

    time.sleep(3)

    typewrite("\nUhhh")

    time.sleep(3)
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
    typewrite("\nNARRATOR:\nYou just woke up and you don't know where you are or your name...")

    time.sleep(3)

    typewrite("\nFredrick:\nAre you alright you just fell from that tree ...\n")

    time.sleep(2)

    typewrite("Whats your name?")

    time.sleep(3)

    typewrite("\nUhhh")

    time.sleep(3)

    typewrite("\nthinking.....")

    time.sleep(3)

    typewrite("\nI don't know")

    time.sleep(3)

    typewrite("\nok ill name you Your name will bee......")

    time.sleep(3)
    name=raw_input("\nWhat will he name you\n")

    time.sleep(3)

    typewrite("\nYour name is {}".format(name))


    time.sleep(3)

    typewrite("\nYou notice the tree you fell from has two doors on it a left and a right door \nthey both lead to a tavern\n")

text()
q3 = raw_input("Left or Right\n").lower()
if "left":
    typewrite("You walk into a smelly tavern.\nThe door locks behind you.")
elif "right":
    typewrite("hihi")



    typewrite("\nthinking.....")

    time.sleep(3)

    typewrite("\nI don't know")

    time.sleep(3)

    typewrite("\nok ill name you Your name will be......")

    time.sleep(3)
    name=input("\n**What will he name you\n")

    time.sleep(3)

    typewrite("\nYour name is {}".format(name))


    time.sleep(3)

    typewrite("\nYou notice the tree you fell from has two doors on it a left and a right door \nthey both lead to a tavern\n")


q3 = input("Left or Right\n").lower()
if q3 =="left":
    typewrite("You walk into a smelly tavern.\nThe door locks behind you.")
    typewrite("\nYou walk into the tarven and a old man is looking at you from across the tavern\nYouw walk towrds him and then somone offers you a drink\n")
question4 = input("***Do you drink or do you walk to the old man\n")
if question4 == "drink":
    #come up with somthing good for this option like posin but make it nice
    typewrite("\nYou drink the cup of coffe and then you relize its posin\nYou wake up in a unfimalry place and don't know whats going on and your head hurts.")
elif question4 == "walk":
    typewrite("\nYou walk to the old man and he says Dear boy Do you wan't to go on an adventrue?\n")
elif q3 =="right":
    typewrite("You walk into a clean tavern. \nThe bar tender offers you a drink")



