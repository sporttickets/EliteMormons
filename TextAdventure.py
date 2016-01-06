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



    typewrite("\nFredrick:\nAre you alright you just fell from that tree ...\n")


    typewrite("Whats your name?")


    typewrite("\nUhhh")

   


    typewrite("\nI don't know")

    

    typewrite("\nok ill name you Your name will bee......")

    time.sleep(1)
    name=raw_input("\nWhat will he name you\n")

    

    typewrite("\nYour name is {}".format(name))




    typewrite("\nYou notice the tree you fell from has two doors on it a left and a right door \nthey both lead to a tavern\n")

text()
q3 = raw_input("Left or Right\n").lower()
if "left":
    return True
    typewrite("You walk into a smelly tavern.\nThe door locks behind you.")
elif "right":
    return False
    typewrite("walk into the rigth door")
else:
    print "that is not an option"




