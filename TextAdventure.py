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


