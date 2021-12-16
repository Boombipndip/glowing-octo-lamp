import time
import random

def game_on():
	print "Welcome to the worst arcade ever"
	print "----------------------------"
	time.sleep(1)
	print "You see two doors. You want room 1 or 2?"
	room = raw_input("Please enter either a 1 or a 2 >")
	if room == "1":
		russian_roulette()
	elif room == "2":
		truth_or_dare()
	else:
		print "But there's only two doors! I don't get it"
		time.sleep(2)
		game_on

def truth_or_dare():
	truth = ["Truth", "truth", 't']
	dare = ["Dare", "dare", "d"]
	yes = ["Yes", "yes", "y"]
	no = ["no", "No", "n"]
	print "Let's play truth or dare!"
	time.sleep(1)
	print "So what will it be? Truth or dare?"
	answer = raw_input("type truth or type dare >")
	if answer in truth:
		print "Truth it is then!"
		time.sleep(1)
		print "OK, let's do this"
		time.sleep(1)
		print "Have you ever kissed anybody? Yes or no?"
		kiss = raw_input(">" )
		if kiss in yes :
			print "EWWWW! Ok you win"
			time.sleep(2)
			game_on()
		elif kiss in no:
			print "Well... maybe someday"
			time.sleep(2)
			game_on()
		else:
			print "I AXED YOU A QUESTION! Quit beating around the bush!"
			time.sleep(2)
			game_on()
	elif answer in dare:
		print "I dare you to play the game in room 1"
		time.sleep(2)
		game_on()
	else: 
		print "A little rich for your blood?"
		time.sleep(1)
		print "Go home to your Commodore 64 then!"
		exit
			
			
def russian_roulette():
	print "Let's play Russian Roulette"
	time.sleep(3)
	print "Spin cylinder now hold the gun to your head"
	time.sleep(2)
	shot = raw_input("Guess a number 1-6 > ")
	trigger = random.randint(1,6)
	if shot == trigger:
		print "BANG. Game Over"
	else:
		print "whew, you deserve a shot of wodka"
	
		
game_on()
