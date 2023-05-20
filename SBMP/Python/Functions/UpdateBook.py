from tkinter import *
from tkinter import messagebox
from mysql.connector import *
from Functions.ViewBooks import *

def updtdb():
    clickedInfo = clicked.get()
    update = updt.get()
    bkid = int(bidInfo.get())

    updtDict = {"Name":"book_name", "Author":"book_author", "Publisher":"book_pub", "ISBN": "book_isbn", "Rent Price":"book_rent_price", "Total Qunatity":"book_total_qty"}
    updtFinal = updtDict[clickedInfo]

    updtQuery = f"UPDATE book_list_master SET {updtFinal}='{update}' where book_id ={bkid};"

    try:
        cur.execute(updtQuery)
        con.commit()
        messagebox.showinfo("Success", "Updated successfully")
    except:
        messagebox.showinfo("Error", "Some error has been occurred")

    win.destroy()

def op():
    global win, con, cur, clicked, updt, bidInfo
    # Adding database details
    con = connect(host = "localhost", user = "root", password = "", database = "lib_mgmt_sys")
    cur = con.cursor()

    # Creating a window
    win = Tk()
    win.title("Library Management System - Update Book")
    win.geometry("800x480")

    # Creating a title and menu frame
    titleFrame = Frame(win, bg = "#005B96")
    titleFrame.place(relx = 0.0, rely = 0.0, relwidth = 1.0, relheight = 0.15)

    menuFrame = Frame(win, bg = "#6497B1")
    menuFrame.place(relx = 0.0, rely = 0.15, relwidth = 1.0, relheight = 0.85)

    # Creating a title heading
    heading = Label(titleFrame, text = "Update Book", font = ("Barlow", 20, "bold"), bg = "#005B96", fg = "white")
    heading.place(relx = 0.50, rely = 0.50, anchor = CENTER)

    # Adding a menu
    options = ["Name", "Author", "Publisher", "ISBN", "Rent Price", "Total Quantity"]
    clicked = StringVar()
    clicked.set("Name")
    selectop = Label(menuFrame, text = "Select operation:", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    selectop.place(relx = 0.40, rely = 0.10, anchor = CENTER)
    drop = OptionMenu(menuFrame, clicked, *options)
    drop.place(relx = 0.60, rely = 0.10, anchor = CENTER)
    updt = Entry(menuFrame)
    updt.place(relx = 0.50, rely = 0.20, anchor = CENTER)

    bid = Label(menuFrame, text = "Book ID:", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    bid.place(relx = 0.40, rely = 0.30, anchor = CENTER)
    bidInfo = Entry(menuFrame)
    bidInfo.place(relx = 0.60, rely = 0.30, anchor = CENTER)

    ViewBooks = Button(menuFrame, text = "View Books", command = viewbk)
    ViewBooks.place(relx = 0.40, rely = 0.45, anchor = CENTER)

    updtBt = Button(menuFrame, text = "Update Book", command = updtdb)
    updtBt.place(relx = 0.60, rely = 0.45, anchor = CENTER)

    win.mainloop()