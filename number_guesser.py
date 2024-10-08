from random import randint
from time import sleep
from os import system

def loading():
	# Loading animations

	for i in range(3): # number selection
		system("cls")
		print("Choosing a really hard number.")
		sleep(0.5)
		system("cls")
		print("Choosing a really hard number..")
		sleep(0.5)
		system("cls")
		print("Choosing a really hard number...")
		sleep(0.5)

	system("cls")

	for i in range(2): # number found
		print("NUMBER SELECTED!")
		sleep(0.3)
		system("cls")
		sleep(0.3)
	print("NUMBER SELECTED!")
	sleep(2)
	system("cls")

def nameReg():
	# function for name registration
	name = str(input("Insert your name: "))
	while name == "": # repeat if the input is an empty string
		print("INVALID NAME, PLEASE TRY AGAIN.")
		sleep(3)
		system("cls")
		name = str(input("Insert your name: "))

	return name.title() # returns the capitalized string after all spaces (ex: "john doe" -> "John Doe")

choice = 1
last_usr = ""

while choice != 0 and choice == 1:
	count = 0 # counts the number of guesses made

	system("cls")
	print("### EPIC NUMBER GUESSING GAME ###")

	name = nameReg()
	if name == last_usr:
		print(f"Welcome back, {name}!")
	else:
		last_usr = name

	x1, x2 = map(int, input(f"{name}, insert an interval [INTEGERS ONLY]\n").split())
	number = randint(x1, x2)
	loading()

	guess = int(input("Choose a number inside that interval: "))
	while guess != number: # loop if the guess is wrong then gives you a small hint, or if the input is invalid
		if guess < x1 and guess > x2:
			print("INVALID NUMBER (not in interval), PLEASE TRY AGAIN\n")
		elif guess > number:
			print("Wrong number! Try a litle lower...\n")
		elif guess < number:
			print("Wrong number! Try a litle higher...\n")
		
		sleep(1)
		system("cls")
		count += 1
		guess = int(input("Choose a number inside that interval: "))
	count += 1 # outside the loop bcs the right guess also counts.
	print(f"YOU GOT IT!!!\nThe number was {number}")
	
	if count == 1:
		print("You guessed the number on first try! (damn, ur good)")
	else:
		print(f"You guessed the number in {count} tries.")

	sleep(5)
	system("cls")

	choice = int(input("Restart? [1 - Yes / 0 - No]"))

system("cls")