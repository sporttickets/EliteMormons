import sys
from time import sleep
def loading(str):
    import sys
    from time import sleep

    for char in str:
        sleep(.02)
        sys.stdout.write(char)
        sys.stdout.flush()


def typewrite(str):
    import sys
    from time import sleep

    for char in str:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()


loading("Loading.................")
import time
time.sleep(0)
typewrite("\nThis game was created by KinCade McCown\n")
time.sleep(1)

typewrite("You just woke up... Hi im alfred i just saw you fall.. whats your name\n")
name= input("Whats your name\n")
typewrite(" Hi {} \n well i have to leave soon so good luck\n".format(name))
typewrite(" {} you see s a gaint tree with two doors a left and a right door ".format(name))
typewrite("\n Do you take the left door or the right door")
option1 = input("Left or Right\n").lower()
if option1 == "left":
    typewrite ("You go to the door and open it slowly and you smell and odor of wizard ...You see people all around but one in particular is looking at you with a face of happines")
    typewrite("You walk to the wizard but then a old handsome i MEAN HANDSOME !MAN offers a DELSIH I MEAN DELISH looking of coco do you take the coco or do you talk to the old wizard who is hot.")
option3 = input("Drink or talk\n").lower()
if option3 == "drink":
    typewrite("You grab that delish looking coco and you drink it but one problem its made for bronies and yoru not a bronie \n anything with a bronie on it is evil savege and bad sir bad")
    typewrite("\n you pass out and you wake up in a house that is not cool.")
elif option1 == "right":
    typewrite("You walk into a room and you are confronted by whirlwin particular smith WPS for short.. he says {} what are u doing here?".format(name))
    tyepwrite("\n You should be doing your quest of EPIC PROPORTIONS")
    typewrite("{} UHH what quest?: Dude are u cearl you need to be slaying some draongs right now so i can make some realy money man\n")
option2 = input("Do the quest or eat some cake?\n").lower()
if option2 =="quest":
    typewrite("you follow young phillips to a carrage")
elif option2 == "eat some cake":
    typewrite("\n You sit down and enjoy some cake")



else: 
    typewrite("Not an optin")

