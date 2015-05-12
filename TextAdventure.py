import sys
from time import sleep

def typewrite(str):
    import sys
    from time import sleep

    for char in str:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

import time
time.sleep(3)
typewrite("You just fell on the ground from the tree you hit your hard really hard... What is your name?")
name = raw_input("	What is your name?	")
#quest = raw_input("What is your quest?	")
#color = raw_input("What is your favorite color?	")

#typewrite"Ah, so your name is {}, your quest is %s, " \
#and your favorite color is %s." % (name, quest, color)
typewrite("Ah, so your name is {}".format(name))
time.sleep(1)


typewrite("\n{} You just woke up. Im suprised to see that you can rember your name.".format(name))
time.sleep(1)

typewrite("Hello By the way im Alfred You look like you hit your head hard on that fall")
time.sleep(1)

typewrite("Alright i will be leaving you good luck {} ".format(name))
time.sleep(1)

typewrite(" NARRATOR:{}. There is a giant tree with two Doors A left Door, and a right Door pick on".format(name))
option1 = raw_input("	Left or the right door\n").lower()
if option1 == "left":
	typewrite("You go to the door and open it slowly and you smell and odor of wizard ...You see people all around but one in particular is looking at you with a face of happines")
	typewrite("You walk to the wizard but then a old handsome i MEAN HANDSOME !MAN offers a DELSIH I MEAN DELISH looking of coco do you take the coco or do you talk to the old wizard who is hot.")
elif option1 == "right":
	typewrite(" not done yet Fool")
else:
	typewrite("that was not an option")

