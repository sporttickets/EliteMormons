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

	answer = input("left Door Or the Right Door").lower()
	if answer == "left":
		print ("You go to the door and open it slowly and you smell and odor of wizard ...You see people all around but one in particular is looking at you with a face of happines")
		print (""+name+"? Glad you could make it good boy come over here and sit down with me")
		print (" when you walk over to the old man somone offers you a delish looking of coco Looks very DELISH. do you take this coco or go talk to the old man")
	elif answer == "Right":
		print ("Right")
	else:
		print ("that was not an option")



game()
