import os

#Sign-up/in system

def getSheetInfo(username, sheetName):
	pass

def getAllSheetInfo(username):
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


def getUserSheetNames(username):
	file = open(getFilePath(username, "master", ".txt"), "r")
	lines = getFileLines(file)
	print(lines)
	return lines

def getAllUsers():
	file = open("./users/master.txt", "r")
	lines = getFileLines(file)
	print(lines)
	return lines

def getPassword(username):
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[1]

def getName(username):
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[2]

def getPronouns(username):
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[3]

def getSchool(username):
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[4]

def getTokens(username):
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	return lines[5]

def getBioInfo(username):
	bio = {}
	bio["username"] = username
	bio["password"] = input("Please enter a password: ")
	bio["name"] = input("Please enter your name: ")
	bio["pronouns"] = input("Please enter your pronouns: ")
	bio["school"] = input("Please enter your school: ")
	bio["sheets"] = []
	return bio

def getFileLines(file):
	lines = []
	for line in file:
		lines.append(line[:-1])
	return lines

def getUserPath(name, ext):
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

def getFilePath(user, file, ext):
	fileName = file + ext
	filePath = ""
	if ext == ".txt":
		filePath = "./users/" + user + "/" + fileName
	"""
	if ext == ".csv":
		filePath = "./fitnessInfo/" + fileName
	if ext == ".jpg":
		filePath = "./images/" + fileName
	"""
	return filePath


def updateSheetMaster(username, sheetName):
	file = open(getFilePath(username, "master", ".txt"), "a")
	file.write(sheetName + "\n")
	file.close()


def addSheet(username):
	sheetName = input("Please enter the name of the sheet: ")
	sheetLink = input("Please enter the link to the sheet: ")
	filePath = getFilePath(username, sheetName, ".txt")
	file = open(filePath, "w+")
	file.write(sheetName + "\n")
	file.write(sheetLink + "\n")
	file.write("0\n")
	file.write("0\n")
	updateSheetMaster(username, sheetName)


def signedIn(username):
	print(getName(username) + ", you are now signed in.")
	enter = ""
	while enter != "exit":
		print("Actions:")
		print("\"add\" to add a sheet to your profile") # needs add sheet function
		print("\"rate\" to rate other sheets")
		print("\"out\" to sign out") # needs sign out function
		print("\"exit\" to exit the application")
		enter = input()
		if enter == "add":
			addSheet(username)
		if enter == "out":
			pass
		if enter == "exit":
			pass


def checkPassword(username, password):
	filePath = getUserPath(username, '.txt')
	file = open(filePath, "r")
	lines = getFileLines(file)
	file.close()
	if lines[1] == password:
		return True
	return False

def writeBio(file, bio):
	keys = list(bio.keys())
	for key in keys:
		print(key)
		if key == "sheets":
			pass
		else:
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

def createUser(username):
	bioInfo = getBioInfo(username)
	os.mkdir("./users/" + username)
	print("Directory " + username + " created")
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

