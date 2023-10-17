#THIS ONLY RUNS ON PYTHON 2

import time

Rooms = {"room1" : "The Gangplank", "room2" : "The Deck", 
"room3" : "The Captain's Quarters", "room4" : "The Treasure Room"}

inventory = ["cutlass", "rum"]

cannon_rooms = ["1", "3"]

yes = ["Yes", "yes", "y", "Yay", "yay"]
no = ["no", "No", "n", "Nay", 'nay']
	
def rob_pirates():
	print "Hello Pirate Pillager"
	time.sleep(1)
	print "Are you ready to go to work?"
	time.sleep(1)
	start = raw_input("Yay or nay? > ")
	if "Y" in start or "y" in start:
		print "ARRRGGGHH LET'S PILLAGE SOME PIRATES!!!"	
		time.sleep(1)
		print "Storm the gangplank!"
		time.sleep(1)
		storm()
	elif "N" in start or "n" in start:
		print "Ye yellow bellied poop deck sweeper,"
		print "drink more rum and come back later"
	else: 
		print "Arrrgh what's that ya said? I don't speak yankee"
		rob_pirates()
		
def storm():
	print "Ye stepped upon the gangplank with your cutlass and rum"
	time.sleep(2)
	print "A pirate says 'well hello sir'"
	time.sleep(2)
	print "Do you fight him or tip your hat and move on?"
	time.sleep(2)
	tip = raw_input("Type f to fight or t to tip your hat > ")
	if tip == "f" or tip == "F":
		print "A parrot poops on your head and distracts you as you"
		print "pull your cutlass."
		time.sleep(3)
		print "the pirate kicks you into the sea"
	elif tip == "t" or "T":
		print "The pirate smiles and you walk past"
		time.sleep(1)
		print "You see a pistol and pick it up"
		inventory.append("Pistol")
		print "Check out your inventory now!"
		print inventory
		time.sleep(2)
		walk_back_to_town()
	else: 
		print "Arrrgh what's that ya said? I don't speak yankee"
		time.sleep(1)
		rob_pirates()
		
def walk_back_to_town():
	print "Since you found a pistol, you can sell it or buy bullets"
	time.sleep(2)
	print "You walk back to town and go to the gun shop"
	time.sleep(2)
	print "The clerk asks you 'What would ye like to do with that gat?'"
	time.sleep(2)
	print "Press 1 to buy bullets or 2 to sell the gun"
	biz = raw_input("> ")
	if biz == str(1):
		inventory.append("Bullets")
		print inventory
		go_to_deck()
	elif biz == str(2):
		inventory.remove("Pistol")
		print inventory
		go_to_deck()
	else:
		print "Arrrgh what's that ya said? I don't speak yankee"
		time.sleep(1)
		go_to_deck()
		
		

def go_to_deck():
	print "You wave your cutlass and announce yer intent to pillage"
	time.sleep(2)
	print "with many a swear word"	
	time.sleep(2)
	print "Three pirates charge you, do you do a leg sweep or chop"
	time.sleep(1)
	print "with your cutlass?"
	time.sleep(3)
	attack1 = raw_input("type l for leg sweep or type c for a chop > ")
	if attack1 == "l":
		print "The leg sweep knocks them all down and now you chop them!"
		time.sleep(2)
		print "But one gets away and you can't get your sword out of"
		print "the dead pirate, WHAT DO YOU DO?"
		time.sleep(2)
		if "Pistol" and "Bullets" in inventory:
			print "You pull your pistol and bang, your troubles are over"
			go_to_captain()
		else: 
			print "You shouldn't have sold that pistol. Now you're headless."
			print "Game Over"
	elif attack1 == "c":
		print "You slice two of them but the third parries your blow"
		time.sleep(3)
		print "the third pirate stabs you"
		time.sleep(3)
		print "This is the bitter end for the Pirate Pillager"
		print "----------------------------------------------"
		time.sleep(2)
		print "GAME OVER"
	else: 
		print "Arrrgh what's that ya said? I don't speak yankee"
		time.sleep(1)
		go_to_deck()

def go_to_captain():
	print "Good job Pirate Pillager, now let's go to the Captain's Quarters"
	time.sleep(3)
	print "You open the door and the captain is passed out drunk with"
	time.sleep(2)
	print "three ladies of the night"
	time.sleep(3)
	print "One of them opens her eyes and gasps loudly..."
	time.sleep(3)
	print "What will you do?"
	choice1 = raw_input("type s to hit her or type k to blow her a kiss > ")
	if choice1 == "s":
		print "Ye be a moron fer sure"
		time.sleep(2)
		print "They all wake up and the captain shoots you"
		time.sleep(2)
		print "This is the bitter end for the Pirate Pillager"
		print "----------------------------------------------"
		time.sleep(1)
		print "GAME OVER"
	elif choice1 == "k":
		print "You blow her a kiss and give her your bottle of rum"
		time.sleep(3)
		print "She smiles and drinks as you creep past them"
		time.sleep(2)
		pick_a_door()
		
def pick_a_door():
	print "You see three doors, hopefully one contains treasure!"
	time.sleep(2)
	pick1 = raw_input("Pick door 1, 2, or 3? > ")
	if pick1 in cannon_rooms:
		print "BOOM!!"
		time.sleep(3)
		print "It was a trap door that set off a cannon"
		time.sleep(3)
		print "You bout dead as hell boy"
		time.sleep(1)
		print "Game Over"
		time.sleep(2)
		print "But wait! It was only a Nerf cannon."
		time.sleep(2)
		print "Try another door"
		pick_a_door()
	elif pick1 == str(2):
		time.sleep(3)
		treasure()
		
def treasure():
	print "ARRRGGHH TREASURE!"
	time.sleep(3)
	print "But there's so much!"
	time.sleep(3)
	print "Do you grab the jewels and the coins or just the jewels?"
	time.sleep(2)
	choice2 = raw_input("type j to just get the jewels or type a to get it all > ")
	if choice2 == "j":
		print "You're dumb but at least you're not greedy"
		time.sleep(3)
		escape()
	elif choice2 == "a":
		print "GOOD CHOICE!"
		time.sleep(2)
		escape()
	else: 
		print "Arrrgh what's that ya said? I don't speak yankee"
		time.sleep(2)
		treasure()	

def escape():
	print "You could sneak back the way you came or you could hop out"
	print "the porthole and swim to shore!"
	time.sleep(3)
	escape1 = raw_input("type s to swim or g to go back how you came > ")
	if escape1 == "s":
		print "Darn ye can't swim while holding treasure can ya"
		time.sleep(2)
		print "Oh well at least ye made it out alive"
		time.sleep(1)
		print "GAME OVER"
	elif escape1 == "g":
		print "You sneak back out and the three ladies of the night follow you"
		time.sleep(3)
		print "SUCCESS!" "ARRRGGGHHH Congrats Pirate Pillager you win!"
	else: 
		print "Arrrgh what's that ya said? I don't speak yankee"
		time.sleep(2)
		escape()
		
rob_pirates()

