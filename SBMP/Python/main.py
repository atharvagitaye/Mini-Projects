from tkinter import *
from tkinter import messagebox
from Functions import *

def verify():
    fnlusr = usrInfo.get()
    fnlpasswd = passwdInfo.get()

    if fnlusr == "Admin" and fnlpasswd == "Admin@123":
        messagebox.showinfo("Successful", "Login Successful")

        lgnwn.destroy()
        hmpage()
    else:
        messagebox.showinfo("Error", "Wrong Credentials")

def hmpage():
    # Creating a window
    win = Tk()
    win.geometry("1280x720")
    win.minsize(width = 1280, height = 720)
    win.title("Library Management System")

    # Giving icon path
    logo = PhotoImage(file = 'Images/Logo.png')
  
    # Setting icon of master window
    win.iconphoto(False, logo)

    # Creating a title and menu frame
    titleFrame = Frame(win, bg = "#005B96")
    titleFrame.place(relx = 0.0, rely = 0.0, relwidth = 1.0, relheight = 0.15)

    menuFrame = Frame(win, bg = "#6497B1")
    menuFrame.place(relx = 0.0, rely = 0.15, relwidth = 1.0, relheight = 0.85)

    # Creating a title heading
    heading = Label(titleFrame, text = "Welcome to \n Absolute Minds Library", font = ("Barlow", 26, "bold"), bg = "#005B96", fg = "white")
    heading.place(relx = 0.50, rely = 0.50, anchor = CENTER)

    # Creating a menu
    adbk = Button(menuFrame, text = "Add Book", command = AddBook.op, bg = "white", fg = "blue", font = ("Barlow", 16))
    adbk.place(relx = 0.50, rely = 0.10, relwidth = 0.15, anchor = CENTER)
    dltbk = Button(menuFrame, text = "Delete Book", command = DeleteBook.op, bg = "white", fg = "blue", font = ("Barlow", 16))
    dltbk.place(relx = 0.50, rely = 0.20, relwidth = 0.15, anchor = CENTER)
    isbk = Button(menuFrame, text = "Issue Book", command = IssueBook.op, bg = "white", fg = "blue", font = ("Barlow", 16))
    isbk.place(relx = 0.50, rely = 0.30, relwidth = 0.15, anchor = CENTER)
    rtnbk = Button(menuFrame, text = "Return Book", command = ReturnBook.op, bg = "white", fg = "blue", font = ("Barlow", 16))
    rtnbk.place(relx = 0.50, rely = 0.40, relwidth = 0.15, anchor = CENTER)
    updtbk = Button(menuFrame, text = "Update Book", command = UpdateBook.op, bg = "white", fg = "blue", font = ("Barlow", 16))
    updtbk.place(relx = 0.50, rely = 0.50, relwidth = 0.15, anchor = CENTER)
    vwbk = Button(menuFrame, text = "View Books", command = ViewBooks.viewbk, bg = "white", fg = "blue", font = ("Barlow", 16))
    vwbk.place(relx = 0.50, rely = 0.60, relwidth = 0.15, anchor = CENTER)
    vwbk = Button(menuFrame, text = "Renter's List", command = RenterList.rntslist, bg = "white", fg = "blue", font = ("Barlow", 16))
    vwbk.place(relx = 0.50, rely = 0.70, relwidth = 0.15, anchor = CENTER)
    prtrcpt = Button(menuFrame, text = "Print Receipt", command = PrintReceipt.op, bg = "white", fg = "blue", font = ("Barlow", 16))
    prtrcpt.place(relx = 0.50, rely = 0.80, relwidth = 0.15, anchor = CENTER)

    win.mainloop()

# Login Page

global lgnwn, usrInfo, passwdInfo

# Creating a login window
lgnwn = Tk()
lgnwn.geometry("480x300")
lgnwn.title("Absolue Minds Library Login")
lgnwn.resizable(0, 0)

# Giving icon path
logolg = PhotoImage(file = "Images/Logo.png")
  
# Setting icon of master window
lgnwn.iconphoto(False, logolg)

# Creating a login page and form frame
ttlFrame = Frame(lgnwn, bg = "#005B96")
ttlFrame.place(relx = 0.0, rely = 0.0, relwidth = 1.0, relheight = 0.15)

mnFrame = Frame(lgnwn, bg = "#6497B1")
mnFrame.place(relx = 0.0, rely = 0.15, relwidth = 1.0, relheight = 0.85)

# Creating a title heading
heading = Label(ttlFrame, text = "Login", font = ("Barlow", 20, "bold"), bg = "#005B96", fg = "white")
heading.place(relx = 0.50, rely = 0.50, anchor = CENTER)

# Creating a form
usr = Label(mnFrame, text = "Username: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
usr.place(relx = 0.40, rely = 0.10, anchor = CENTER)
usrInfo = Entry(mnFrame)
usrInfo.place(relx = 0.60, rely = 0.10, anchor = CENTER)

passwd = Label(mnFrame, text = "Password: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
passwd.place(relx = 0.40, rely = 0.25, anchor = CENTER)
passwdInfo = Entry(mnFrame, show = "*")
passwdInfo.place(relx = 0.60, rely = 0.25, anchor = CENTER)

lgBtn = Button(mnFrame, text = "Login", font = ("Barlow", 10), command = verify)
lgBtn.place(relx = 0.50, rely = 0.40, anchor = CENTER)

lgnwn.mainloop()