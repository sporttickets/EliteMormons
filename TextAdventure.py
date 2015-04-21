def game():
	print ("Hello")
	import time
	time.sleep(3)

	name = input("What is your name")
	print ("Welcome, "+name+"")
	time.sleep(3)

	print (""+name+" You just woke up. Im suprised to see that you can rember your name.") 
	time.sleep(3) 
	print ("Hello By the way im Alfred You look like you hit your head hard on that fall")
	time.sleep(3)

	print ("Alright i will be leaving you good luck "+name+"")
	time.sleep(5)

	print (""+name+" There is a giant tree with two Doors A left Door, and a right Door pick on")

	answer = input("left Or the Right ").lower()
	if answer == "left":
		print ("	You go to the door and open it slowly and you smell and odor of wizard ...You see people all around but one in particular is looking at you with a face of happines")
		time.sleep(4)

		print (""+name+"? 	Glad you could make it good boy come over here and sit down with me")
		time.sleep(3)

		print (" 	when you walk over to the old man somone offers you a delish looking of coco Looks very DELISH. do you take this coco or go talk to the old man")
		time.sleep(3)

	answer2 = input("Drink or talk").lower()
	import time
	if answer2 == "drink":
		print ("	You Grab that Delish looking of coco and you taste it and you notice it is very sweat and you enjoy it to much ITS TO DELISH TO SWEET o no ")
		time.sleep(3)

		print ("you passed out and you woke up and you can't rember your name..")
	elif answer2 == "talk":
		print ("Hi "+name+" What are you doing here you looked like you hit your head hard on that fall -_-")
	print ("what fall i don't rember a fall what are you talking about and why didin't i drink that dleish looking coco i mean it probs better anything you have to say right now")
	time.sleep(3)
	print ("I don't like this becuase im thirsty and cold...")
	print ("Oldman: wtf its 101 tempture in this chicken.")
	fall = input("What do you know about the fal ffs -_-")
	print (""+fall+"")
	elif answer == "Right":
		print ("Right")
	else:
		print ("that was not an option")



game()
