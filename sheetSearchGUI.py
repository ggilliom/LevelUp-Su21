from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkhtmlview import HTMLLabel
from tkinter import messagebox
import random
# test
from sheetScrape import importList
import back as b

#Stores user info in tuples of name and password...
userList = []

#Test Values for until Garrett finishes Backend...
testName = "Jake"
testPwd = "123"
testRatings = [1, 2, 3, 4, 5]
testSource = "kutasoftware.com"
testTokens = 13

#Main program...
root = Tk()
root.title('Sheet Search')
root.iconbitmap('9iRb8Xq6T.ico')
root.geometry("200x200")

#For errors...
signinError = "Incorrect username or password."
signupError = "Please make sure passwords match."
def popup(error):
    messagebox.showerror("Oops!", error)
    return

#For getting rid of a window...
def exitProgram(root):
    root.destroy()
    return

#For opening login page...
def openLogin():
    top = Toplevel()
    top.title('Login Page')
    top.geometry("700x600")
    #Make frame for login...
    loginFrame = LabelFrame(top, padx=50, pady=50)
    loginFrame.pack(padx=100, pady=100)

    #Populate loginFrame w/ Labels...
    userLabel = Label(loginFrame, text="Username: ")
    pwdLabel = Label(loginFrame, text="Password: ")

    userLabel.grid(row=0, column=0)
    pwdLabel.grid(row=1, column=0)

    #Populate loginFrame w/ Input Bars...
    userEntry = Entry(loginFrame)
    pwdEntry = Entry(loginFrame)

    userEntry.grid(row=0, column=3)
    pwdEntry.grid(row=1, column=3)

    #Populate loginFrame w/ Submit Button...
    submitButton = Button(loginFrame, text="Submit", command = lambda: [submitInfo(userEntry, pwdEntry, top)])
    submitButton.grid(row=2, column=2)

    #Make frame for new users...
    newbieFrame = LabelFrame(top, padx=10, pady=10)
    newbieFrame.pack(padx=20, pady=20)

    #Populate newbieFrame w/ Label...
    registerLabel = Label(newbieFrame, text="New to SheetSearch?")
    registerLabel.pack()

    #Populate newbieFrame w/ Register Button...
    registerButton = Button(newbieFrame, text="Sign Up", command= lambda: [signUp(), exitProgram(top)])
    registerButton.pack(padx=10, pady=10)

    return

#For submitting info...
def submitInfo(name, pwd, root):

    #if tempName == Backend.getName() and tempPwd = Backend.getPwd():
    if (name.get() == testName and pwd.get() == testPwd):
        openHomePage()
        root.destroy()
    else:
        popup(signinError)
        root.destroy()
        openLogin()

    return

#For signing up...
def signUp():

    top = Toplevel()
    top.title('Registration')
    top.geometry("700x500")

    #Make frame for login...
    registrationFrame = LabelFrame(top, padx=50, pady=50)
    registrationFrame.pack(padx=100, pady=100, expand=True)

    #Populate loginFrame w/ Labels...
    userLabel = Label(registrationFrame, text="Enter username: ")
    pwdLabel = Label(registrationFrame, text="Enter password: ")
    confPwdLabel = Label(registrationFrame, text="Confirm password: ")

    userLabel.grid(row=0, column=0)
    pwdLabel.grid(row=1, column=0)
    confPwdLabel.grid(row=2, column=0)

    #Populate loginFrame w/ Input Bars...
    userEntry = Entry(registrationFrame)
    pwdEntry = Entry(registrationFrame)
    confPwdEntry = Entry(registrationFrame)

    userEntry.grid(row=0, column=3)
    pwdEntry.grid(row=1, column=3)
    confPwdEntry.grid(row=2, column=3)

    registrationButton = Button(registrationFrame, text="Register", command= lambda: [enterInfo(userEntry.get(), pwdEntry.get(), confPwdEntry.get()), exitProgram(top)])
    registrationButton.grid(row=3, column=2)

    return

#For registering users and storing their info...
def enterInfo(name, pwd, cpwd):
    if pwd == cpwd:
        userTuple = (name, pwd)
        userList.append(userTuple) #BACKEND: Store tuple as user file...
        openHomePage()
    else:
        popup(signupError)
        signUp()

#For opening homepage...
def openHomePage():
    top = Toplevel()
    top.title('Home')
    top.geometry("400x500")

    libraryButton = Button(top, text="Sheet Library", command = lambda: [openLibrary(), top.destroy()])
    libraryButton.pack()

    profileButton = Button(top, text="Profile", command = lambda: [openProfile(), top.destroy()])
    profileButton.pack()

    quitButton = Button(top, text="Quit", command = lambda: top.destroy())
    quitButton.pack()

    return

#For opening worksheet library...
def openLibrary():
    testName = "Jake"
    testPwd = "123"
    testRatings = [1, 2, 3, 4, 5]
    testSource = "kutasoftware.com"

    top = Toplevel()
    top.title('Worksheet Library')
    top.geometry("1000x800")

    #Create a main frame
    main_frame = Frame(top)
    main_frame.pack(fill=BOTH, expand=1)

    #Create a canvas
    my_Canvas = Canvas(main_frame)
    my_Canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #Add a scrollbar
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_Canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    #Configure the canvas
    my_Canvas.configure(yscrollcommand=my_scrollbar.set)
    my_Canvas.bind('<Configure>', lambda e: my_Canvas.configure(scrollregion = my_Canvas.bbox("all")))

    #Create another frame inside the canvas
    second_frame = Frame(my_Canvas)

    #Add that New frame to a window in the canvas
    my_Canvas.create_window((0,0), window=second_frame, anchor="nw")

    #Frame for both links and ratings...
    entireFrame = LabelFrame(second_frame)
    entireFrame.pack()

    #Home button...
    homeFrame = LabelFrame(entireFrame)
    homeFrame.grid(row=1, column=2)

    returnHomeButton = Button(homeFrame, text="Home", command= lambda: [openHomePage(), top.destroy()])
    returnHomeButton.pack()

    #Links...
    linkFrame = LabelFrame(entireFrame)
    linkFrame.grid(row=2, column=1)

    #Sources...
    sourceFrame = LabelFrame(entireFrame)
    sourceFrame.grid(row=2, column=2)

    #Ultimate rating frame...
    ultRatingFrame = LabelFrame(entireFrame)
    ultRatingFrame.grid(row=2, column=3)

    #List of items with their url, source, and rating...
    for i, j, k in importList: #NEEDS TO BE MODIFIED...
        disableVar = ACTIVE
        def disableButton():
            disableVar = DISABLED
            return

        #links...
        linkLabel = HTMLLabel(linkFrame, html='<a href="{}"> {} </a>'.format(i, j), borderwidth=5, height=2, width=50, relief=RIDGE)
        linkLabel.pack()

        #Sources,,,
        sourceLabel = Label(sourceFrame, text="Source: {}".format(testSource), borderwidth=5, height=2, width=50, relief=RIDGE)
        sourceLabel.pack()

        #Ratings...
        ratingFrame = LabelFrame(ultRatingFrame)
        ratingFrame.pack()

        randomRating = random.choice(testRatings)
        ratingLabel = Label(ratingFrame, text="Rating: {}".format(str(randomRating)), borderwidth=5, height=1, width=50, relief=RIDGE)
        ratingLabel.grid(row=1, column=1)

        finalRatingsFrame = LabelFrame(ratingFrame, relief=RIDGE)
        finalRatingsFrame.grid(row=1, column=2)

        rateInput = Entry(finalRatingsFrame, borderwidth=5, width=4, relief=RIDGE)
        rateInput.grid(row=1, column=1)

        rateButton = Button(finalRatingsFrame, text="Rate", command = lambda: [rateSheet(j, rateInput.get()), disableButton()], borderwidth=5, height=2, width=4, relief=RAISED, state=disableVar)
        rateButton.grid(row=1, column=2)
    #Use sorted sheet list to create search hierarchy w/ dropdown menu...

#For rating sheets...
def rateSheet(sheetName, rating):
    #...
    return

#For opening profile page
def openProfile():
    top = Toplevel()
    top.title('Login Page')
    top.geometry("700x600")

    nameLabel = Label(top, text="Username: {}".format(testName))
    nameLabel.pack()

    tokenLabel = Label(top, text="Tokens: {}".format(testTokens))
    tokenLabel.pack()

    returnHomeButton = Button(top, text="Home", command= lambda: [openHomePage(), top.destroy()])
    returnHomeButton.pack()

    #Space to upload link...

    return

startButton = Button(text="Start", command=openLogin)
startButton.pack()

quitButton = Button(text="Quit", command=root.destroy)
quitButton.pack()

#Finish GUI...
root.mainloop()
