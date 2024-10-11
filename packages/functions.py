from random import randint
from time import sleep
from os import system

def loading():
	""" Loading animations """

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
	""" function for name registration """

	name = str(input("Insert your name\n> "))
	while name == "": # repeat if the input is an empty string
		print("INVALID NAME, PLEASE TRY AGAIN.")
		sleep(3)
		system("cls")
		name = str(input("Insert your name\n> "))

	return name.title() # returns the capitalized string after all spaces (ex: "john doe" -> "John Doe")