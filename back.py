import os

#Sign-up/in system

def getRatingAvg(username, sheetName): # returns average rating for a sheet
	sheet = getSheetInfo(username, sheetName)
	average = int(sheet["total"])/int(sheet["numRatings"])
	return round(average, 1)

def applyRating(username, sheetName, rating): # applies a rating to a sheet
	sheet = getSheetInfo(username, sheetName)
	file = open(getFilePath(username, sheetName, ".txt"), "w+")
	file.write(sheet["name"] + "\n")
	file.write(sheet["link"] + "\n")
	total = int(sheet["total"]) + int(rating)
	file.write(str(total) + "\n")
	numRatings = int(sheet["numRatings"]) + 1
	file.write(str(numRatings) + "\n")
	file.close()


def rateSheet(): # terminal front end for sheet rating
	print("Here is a list of all of our sheets:\n")
	displaySheets()
	allSheets = getAllSheets()
	sheet = input("Enter the sheet you'd like to rate: ")
	rating = input("Enter your rating for the sheet: ")
	applyRating(allSheets[sheet], sheet, rating)

def getAllSheets(): # returns list of sheets in (sheet, user) form
	users = getAllUsers()
	userSheets = {}
	allSheets = {}
	for user in users:
		sheets = getUserSheetNames(user)
		userSheets[user] = sheets
	for key in userSheets.keys():
		for sheet in userSheets[key]:
			allSheets[sheet] = key
	return(allSheets)


def displaySheets(): # displays all sheets under each user
	users = getAllUsers()
	userSheets = {}
	for user in users:
		sheets = getUserSheetNames(user)
		userSheets[user] = sheets
	for key in userSheets.keys():
		print(key + ":")
		for sheet in userSheets[key]:
			print(sheet)



def getSheetInfo(username, sheetName): # returns dictionary of sheet info for a specified sheet
	file = open(getFilePath(username, sheetName, ".txt"), "r")
	lines = getFileLines(file)
	name = lines[0]
	link = lines[1]
	total = lines[2]
	numRatings = lines[3]
	sheet = {
			"name": name,
			"link": link,
			"total": total,
			"numRatings": numRatings
		}
	file.close()
	return sheet

def getAllSheetInfo(username): # returns dictionary of info for all of a user's sheets
	sheetNames = getUserSheetNames(username)
	sheets = {}
	for sheet in sheetNames:
		file = open(getFilePath(username, sheet, ".txt"), "r")
		lines = getFileLines(file)
		name = lines[0]
		link = lines[1]
		total = lines[2]
		numRatings = lines[3]
		sheets[sheet] = {
			"name": name,
			"link": link,
			"total": total,
			"numRatings": numRatings
		}
	return sheets


def getUserSheetNames(username): # returns all sheet names for a user
	file = open(getFilePath(username, "master", ".txt"), "r")
	lines = getFileLines(file)
	#print(lines)
	return lines

def getAllUsers(): # returns usernames of all users
	file = open("./users/master.txt", "r")
	lines = getFileLines(file)
	#print(lines)
	return lines

def getPassword(username): # returns the password of a user
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[1]

def getName(username): # returns name of user
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[2]

def getPronouns(username): # returns pronouns of user
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[3]

def getSchool(username): # returns school of user
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[4]

def getTokens(username): # returns number of tokens for a user
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[5]

def getFileLines(file): # returns lines of a file in list form
	lines = []
	for line in file:
		lines.append(line[:-1])
	return lines

def getUserPath(name, ext): # returns filepath to a user's data file
	fileName = name + ext
	filePath = ""
	if ext == ".txt":
		filePath = "./users/" + name + "/" + fileName
	return filePath

def getFilePath(user, file, ext): # returns filepath to a file in a user's directory
	fileName = file + ext
	filePath = ""
	if ext == ".txt":
		filePath = "./users/" + user + "/" + fileName
	return filePath


def updateSheetMaster(username, sheetName): # updates list of sheets for a user when a sheet is created
	file = open(getFilePath(username, "master", ".txt"), "a")
	file.write(sheetName + "\n")
	file.close()


def createSheet(username, sheetName, sheetLink): # creates a sheet and updates sheet master
	filePath = getFilePath(username, sheetName, ".txt")
	file = open(filePath, "w+")
	file.write(sheetName + "\n")
	file.write(sheetLink + "\n")
	file.write("0\n")
	file.write("0\n")
	file.close()
	updateSheetMaster(username, sheetName)


def addSheet(username): # terminal frontend for adding a sheet
	sheetName = input("Please enter the name of the sheet: ")
	sheetLink = input("Please enter the link to the sheet: ")
	createSheet(username, sheetName, sheetLink)


def signedIn(username): # terminal front end for being signed in
	print(getName(username) + ", you are now signed in.")
	enter = ""
	while enter != "exit":
		print("Actions:")
		print("\"add\" to add a sheet to your profile") # needs add sheet function
		print("\"rate\" to rate other sheets")
		print("\"display\" to display sheets")
		print("\"out\" to sign out") # needs sign out function
		print("\"exit\" to exit the application")
		enter = input()
		if enter == "add":
			addSheet(username)
		if enter == "rate":
			rateSheet()
		if enter == "display":
			displaySheets()
		if enter == "out":
			pass
		if enter == "exit":
			pass


def checkPassword(username, password): # checks if entered password for a username is correct
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	if lines[1] == password:
		return True
	return False

def inputBioInfo(username): # input bio info and return it in dictionary form
	bio = {}
	bio["username"] = username
	bio["password"] = input("Please enter a password: ")
	bio["name"] = input("Please enter your name: ")
	bio["pronouns"] = input("Please enter your pronouns: ")
	bio["school"] = input("Please enter your school: ")
	return bio

def writeBio(file, bio):
	keys = list(bio.keys())
	for key in keys:
		print(key)
		file.write(bio[key] + "\n")
	file.write("0")

def updateMaster(username):
	file = open("./users/master.txt", "a")
	file.write(username)
	file.write("\n")
	file.close()

def createMasterSheet(username):
	file = open(getFilePath(username, "master", ".txt"), "w+")
	file.close()

def createUser(username, bioInfo): # creates a user, bioInfo is a dictionary of info created with format from inputBioInfo()
	os.mkdir("./users/" + username)
	#print("Directory " + username + " created")
	file = open(getUserPath(username, '.txt'), "w+")
	updateMaster(username)
	writeBio(file, bioInfo)
	file.close()
	createMasterSheet(username)

def doesUserExist(username, ext):
	filePath = getUserPath(username, ext)
	try:
		file = open(filePath, "r+")
	except:
		return False
	file.close()
	return True

def isNameFree(username, ext):
	filePath = getUserPath(username, ext)
	try:
		file = open(filePath,  "r+")
	except:
		return True
	file.close()
	return False


def signIn():
	print("signIn")
	username = input("Please enter your username: ")
	exists = doesUserExist(username, '.txt') # checks if username is in database already
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
	bioInfo = inputBioInfo(username)
	userInfo = createUser(username, bioInfo)
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

