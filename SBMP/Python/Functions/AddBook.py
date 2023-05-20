from tkinter import *
from tkinter import messagebox
from PIL import *
from mysql.connector import *

def adbkdb():
    bname = nameInfo.get()
    authname = authInfo.get()
    pubname = pubInfo.get()
    isbnname = isbnInfo.get()
    rntprcdb = rntprcInfo.get()
    ttlqtydb = ttlqtyInfo.get()

    insertBook = f"INSERT INTO `book_list_master` (`book_id`, `book_name`, `book_author`, `book_pub`, `book_isbn`, `book_rent_price`, `book_total_qty`, `book_avlb_qty`, `book_status`) VALUES ('','{bname}','{authname}','{pubname}','{isbnname}','{rntprcdb}','{ttlqtydb}','{ttlqtydb}','1');"

    try:
        cur.execute(insertBook)
        con.commit()
        messagebox.showinfo("Successful", "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add book")

    win.destroy()

def op():
    global win, con, cur, nameInfo, authInfo, pubInfo, isbnInfo, rntprcInfo, ttlqtyInfo

    # Adding database details
    con = connect(host = "localhost", user = "root", password = "", database = "lib_mgmt_sys")
    cur = con.cursor()

    # Creating a window
    win = Tk()
    win.title("Library Management System - Add Book")
    win.geometry("800x480")
    win.minsize(width = 800, height = 480)

    # Creating a title and menu frame
    titleFrame = Frame(win, bg = "#005B96")
    titleFrame.place(relx = 0.0, rely = 0.0, relwidth = 1.0, relheight = 0.15)

    menuFrame = Frame(win, bg = "#6497B1")
    menuFrame.place(relx = 0.0, rely = 0.15, relwidth = 1.0, relheight = 0.85)

    # Creating a title heading
    heading = Label(titleFrame, text = "Add Book", font = ("Barlow", 20, "bold"), bg = "#005B96", fg = "white")
    heading.place(relx = 0.50, rely = 0.50, anchor = CENTER)

    # Creating a form
    name = Label(menuFrame, text = "Name: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    name.place(relx = 0.40, rely = 0.10, anchor = CENTER)
    nameInfo = Entry(menuFrame)
    nameInfo.place(relx = 0.60, rely = 0.10, anchor = CENTER)

    auth = Label(menuFrame, text = "Author: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    auth.place(relx = 0.40, rely = 0.20, anchor = CENTER)
    authInfo = Entry(menuFrame)
    authInfo.place(relx = 0.60, rely = 0.20, anchor = CENTER)

    pub = Label(menuFrame, text = "Publisher: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    pub.place(relx = 0.40, rely = 0.30, anchor = CENTER)
    pubInfo = Entry(menuFrame)
    pubInfo.place(relx = 0.60, rely = 0.30, anchor = CENTER)

    isbn = Label(menuFrame, text = "ISBN: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    isbn.place(relx = 0.40, rely = 0.40, anchor = CENTER)
    isbnInfo = Entry(menuFrame)
    isbnInfo.place(relx = 0.60, rely = 0.40, anchor = CENTER)

    rntprc = Label(menuFrame, text = "Rent Price: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    rntprc.place(relx = 0.40, rely = 0.50, anchor = CENTER)
    rntprcInfo = Entry(menuFrame)
    rntprcInfo.place(relx = 0.60, rely = 0.50, anchor = CENTER)

    ttlqty = Label(menuFrame, text = "Total Quantity: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    ttlqty.place(relx = 0.40, rely = 0.60, anchor = CENTER)
    ttlqtyInfo = Entry(menuFrame)
    ttlqtyInfo.place(relx = 0.60, rely = 0.60, anchor = CENTER)

    SubmitBtn = Button(menuFrame, text = "Add Book", font = ("Barlow", 10), command = adbkdb)
    SubmitBtn.place(relx = 0.50, rely = 0.75, anchor = CENTER)

    win.mainloop()