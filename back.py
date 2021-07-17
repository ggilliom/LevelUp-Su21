import os

#Sign-up/in system

def getName(username):
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[2]

def getFileLines(file):
	lines = []
	for line in file:
		lines.append(line[:-1])
	return lines

def getFilePath(name, ext):
	fileName = name + ext
	filePath = ""
	if ext == ".txt":
		filePath = "./users/" + name + "/" + fileName
	"""
	if ext == ".csv":
		filePath = "./fitnessInfo/" + fileName
	if ext == ".jpg":
		filePath = "./images/" + fileName
	"""
	return filePath

def signedIn(username):
	print(getName(username) + ", you are now signed in.")

def checkPassword(username, password):
	filePath = getFilePath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	if lines[1] == password:
		return True
	return False

def createUser(username):
	pass
	#testing
	#TODO, gonna be more stuff besides this but figure out on ur own!

def doesUserExist(username, ext):
	filePath = getFilePath(username, ext)
	try:
		file = open(filePath, "r+")
	except:
		return False
	file.close()
	return True

def isNameFree(username, ext):
	filePath = getFilePath(username, ext)
	try:
		file = open(filePath,  "r+")
	except:
		return True
	file.close()
	return False

def signedIn(username):
	print(getName(username) + ", you are now signed in.")


def signIn():
	print("signIn")
	username = input("Please enter your username: ")
	exists = doesNameExist(username, '.txt') # checks if username is in database already
	if exists:
		password = input("Please enter your password: ")
		isCorrect = checkPassword(username, password)
		if isCorrect:
			print("Username and password accepted. Welcome, " + getName(username))
			signedIn(username)
		else:
			print("Incorrect password.")

	else:
		print("That username does not exist in our database. Would you like to sign up?")
		choice = input("Enter \"yes\" or \"no\": ")
		if choice == "yes":
			signUp()
		else:
			print("Have a nice day!")


def signUp(): 
	print("signUp")
	username = input("Please enter your username: ")
	available = isNameFree(username, '.txt') # checks if the username is free
	#print(available)
	while not available:
		print("The username \"" + username + "\" already exists. Please try another one")
		username = input("Please enter another username: ")
		available = isNameFree(username, '.txt')
	print("That username is available!")
	userInfo = createUser(username)
	choice = input("Would you like to sign in? Enter \"yes\" or \"no\": ")
	if choice == "yes":
		signIn()
	else:
		print("Have a nice day!")


def main():
	print("Hello and welcome to Sheet Search!")
	print("Would you like to sign in or sign up?")
	userChoice = input("Please enter \"in\" or \"up\": ")

	while not (userChoice == "in" or userChoice == "up"):
		userChoice = input("Input error; type \"in\" or \"up\": ")

	if userChoice == "in":
		print("The User wants to sign in")
		signIn()
	else:
		print("The User wants to sign up")
		signUp()

