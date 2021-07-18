from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkhtmlview import HTMLLabel
from tkinter import messagebox
import random
# test
from sheetScrape import importList
import back as b


global_name = ''
user_info = {}

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
    registerButton = Button(newbieFrame, text="Sign Up", command= lambda: [signUp0(), exitProgram(top)])
    registerButton.pack(padx=10, pady=10)

    return

#For submitting info...
def submitInfo(name, pwd, root):
    global global_name
    username = name.get()
    exists = not(b.isNameFree(username, '.txt'))
    password = pwd.get()

    print(exists)

    if exists:
        is_right = b.checkPassword(username, password)
        if is_right:
            openHomePage()
            root.destroy()
            return
    
    popup(signinError)
    root.destroy()
    global_name = name
    openLogin()


#For signing up...
def signUp0():

    top = Toplevel()
    top.title('Registration')
    top.geometry("700x500")

    #Make frame for login...
    registrationFrame = LabelFrame(top, padx=50, pady=50)
    registrationFrame.pack(padx=100, pady=100, expand=True)

    #Populate loginFrame w/ Labels...
    userLabel = Label(registrationFrame, text="Enter username: ").grid(row=0, column=0)
    pwdLabel = Label(registrationFrame, text="Enter password: ").grid(row=1, column=0)
    confPwdLabel = Label(registrationFrame, text="Confirm password: ").grid(row=2, column=0)

    #Populate loginFrame w/ Input Bars...
    userEntry = Entry(registrationFrame)
    pwdEntry = Entry(registrationFrame)
    confPwdEntry = Entry(registrationFrame)

    userEntry.grid(row=0, column=3)
    pwdEntry.grid(row=1, column=3)
    confPwdEntry.grid(row=2, column=3)

    registrationButton = Button(registrationFrame, text="Continue", command= lambda: [enterInfo(userEntry.get(), pwdEntry.get(), confPwdEntry.get()), exitProgram(top)])
    registrationButton.grid(row=3, column=2)

    #return

    #For registering users and storing their info...
    def enterInfo(name, pwd, cpwd):
        global user_info
        global global_name
        if not(b.isNameFree(name, '.txt')):
            popup("That username is already taken!")
            signUp0()
            return
        # if password matches in both boxes
        if pwd != cpwd:
            popup(signupError)
            signUp0()
            return

            #userTuple = (name, pwd)
            #userList.append(userTuple) #BACKEND: Store tuple as user file...
        global_name = name
        user_info['username'] = name
        user_info['pwd'] = pwd
        signUp1()
        
def signUp1():
    top = Toplevel()
    top.title('Registration1')
    top.geometry("700x500")

    #Make frame for login...
    registrationFrame = LabelFrame(top, padx=50, pady=50)
    registrationFrame.pack(padx=100, pady=100, expand=True)

    # add another data filed to this list and label will be created and its entry will be passed to function to be written to .txt file
    fields = ["age", "pronouns", "school"]
    entries = []
    for i in range(len(fields)):
        Label(registrationFrame, text="Enter your {}".format(fields[i])).grid(row=i, column=0)
        entries.append(Entry(registrationFrame))
        entries[i].grid(row=i, column=3)

    registrationButton = Button(registrationFrame, text="Register", command= lambda: [enterInfo([e.get() for e in entries]), exitProgram(top)])
    registrationButton.grid(row=3, column=2)

    def enterInfo(args):
        global user_info
        for i in range(len(args)):
            user_info[i] = args[i]
        b.createUser(global_name, user_info)
        openHomePage()


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

    all_users = b.getAllUsers()

    widgets_and_data = []
    f = open("users/sheets_to_user_name.txt", "w+")
    #List of items with their url, source, and rating...
    for i, j, k in importList: #NEEDS TO BE MODIFIED...
        index = 0

        # i just ran this one to assign a username to all of these sheets...
  
        '''      
        rand_user = random.choice(all_users)
        b.createSheet(rand_user, j, k)
        
        f.write(j + "\n")
        f.write(rand_user + "\n")
        f.write("\n")
        '''




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

        rateButton = Button(finalRatingsFrame, text="Rate", command = lambda: [rateSheet(index), disableButton()], borderwidth=5, height=2, width=4, relief=RAISED, state=disableVar)
        rateButton.grid(row=1, column=2)

        widgets_and_data.append([rateButton, rateInput, j])
        index += 1
    #Use sorted sheet list to create search hierarchy w/ dropdown menu...
    f.close()
    #For rating sheets...
    def rateSheet(index):
        #...
        b.applyRating(b.get_user_by_sheet(widgets_and_data[index][2]), widgets_and_data[index][2], widgets_and_data[index][1])

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
