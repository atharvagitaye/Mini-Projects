from tkinter import *
from tkinter import messagebox
from mysql.connector import *
from Functions.ViewBooks import *

def dltbkdb():
    bid = idInfo.get()

    deleteBook = f"DELETE FROM book_list_master WHERE book_id={bid};"

    try:
        cur.execute(deleteBook)
        con.commit()
        messagebox.showinfo("Successful", "Book deleted successfully")
    except:
        messagebox.showinfo("Error", "Some error has been occured \nCan't delete book")

    win.destroy()

def op():
    global win, con, cur, idInfo

    # Adding database details
    con = connect(host = "localhost", user = "root", password = "", database = "lib_mgmt_sys")
    cur = con.cursor()

    # Creating a window
    win = Tk()
    win.title("Library Management System - Delete Book")
    win.geometry("800x480")
    win.minsize(width = 800, height = 480)

    # Creating a title and menu frame
    titleFrame = Frame(win, bg = "#005B96")
    titleFrame.place(relx = 0.0, rely = 0.0, relwidth = 1.0, relheight = 0.15)

    menuFrame = Frame(win, bg = "#6497B1")
    menuFrame.place(relx = 0.0, rely = 0.15, relwidth = 1.0, relheight = 0.85)

    # Creating a title heading
    heading = Label(titleFrame, text = "Delete Book", font = ("Barlow", 20, "bold"), bg = "#005B96", fg = "white")
    heading.place(relx = 0.50, rely = 0.50, anchor = CENTER)

    # Creating a form
    id = Label(menuFrame, text = "ID: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    id.place(relx = 0.40, rely = 0.10, anchor = CENTER)
    idInfo = Entry(menuFrame)
    idInfo.place(relx = 0.60, rely = 0.10, anchor = CENTER)

    ViewBooks = Button(menuFrame, text = "View Books", font = ("Barlow", 10), command = viewbk)
    ViewBooks.place(relx = 0.40, rely = 0.25, anchor = CENTER)

    SubmitBtn = Button(menuFrame, text = "Delete Book", font = ("Barlow", 10), command = dltbkdb)
    SubmitBtn.place(relx = 0.60, rely = 0.25, anchor = CENTER)

    win.mainloop()