from tkinter import *
from mysql.connector import *

def viewbk():
    l1 = []
    # Creating a window
    win = Tk()
    win.title("Library Management System - View Books")
    win.geometry("1200x480")
    win.minsize(width = 800, height = 480)

    # Adding database details
    con = connect(host = "localhost", user = "root", password = "", database = "lib_mgmt_sys")
    cur = con.cursor()

    extractdt = "SELECT * FROM book_list_master;"
    cur.execute(extractdt)
    result = cur.fetchall()

    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 0, row = 0)
    Label(frame, text = "ID", width = 15, font = ("Barlow", 10, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 1, row = 0)
    Label(frame, text = "Name", width = 15, font = ("Barlow", 10, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 2, row = 0)
    Label(frame, text=f"Author", width = 15, font = ("Barlow", 10, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 3, row = 0)
    Label(frame, text=f"Publisher", width = 15, font = ("Barlow", 10, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 4, row = 0)
    Label(frame, text=f"ISBN", width = 15, font = ("Barlow", 10, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 5, row = 0)
    Label(frame, text=f"Rent Price", width = 15, font = ("Barlow", 10, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 6, row = 0)
    Label(frame, text=f"Total Quantity", width = 15, font = ("Barlow", 10, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 7, row = 0)
    Label(frame, text = "Available Quantity", width = 15, font = ("Barlow", 10, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 8, row = 0)
    Label(frame, text = "Available Status", width = 15, font = ("Barlow", 10, "bold")).pack()

    for i in range(9):
        for j in result:
            l1.append(j[i])

        max = len(l1)

        for k in range(max):
            frame = Frame(win, relief = RAISED, borderwidth = 1)
            frame.grid(column = i, row = k+1)
            Label(frame, text = l1[k], width = 15, font = ("Barlow", 10)).pack()

        l1.clear()

    win.mainloop()