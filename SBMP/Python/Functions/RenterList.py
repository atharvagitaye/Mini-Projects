from tkinter import *
from mysql.connector import *

def rntslist():
    l1 = []
    # Creating a window
    win = Tk()
    win.title("Library Management System - View Books")
    win.geometry("1500x480")
    win.minsize(width = 800, height = 480)

    # Adding database details
    con = connect(host = "localhost", user = "root", password = "", database = "lib_mgmt_sys")
    cur = con.cursor()

    extractdt = "SELECT * FROM book_rent_master;"
    cur.execute(extractdt)
    result = cur.fetchall()

    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 0, row = 0)
    Label(frame, text = "Transaction ID", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 1, row = 0)
    Label(frame, text = "Name", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 2, row = 0)
    Label(frame, text=f"Age", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 3, row = 0)
    Label(frame, text=f"Renting Date", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 4, row = 0)
    Label(frame, text=f"Promised \nReturn Date", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 5, row = 0)
    Label(frame, text=f"Return Date", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 6, row = 0)
    Label(frame, text=f"Rent Status", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 7, row = 0)
    Label(frame, text=f"Address \nLine 1", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 8, row = 0)
    Label(frame, text=f"Address \nLine 2", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 9, row = 0)
    Label(frame, text=f"Pincode", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 10, row = 0)
    Label(frame, text=f"Contact No", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 11, row = 0)
    Label(frame, text=f"Email", width = 15, font = ("Barlow", 8, "bold")).pack()
    frame = Frame(win, relief = RAISED, borderwidth = 1)
    frame.grid(column = 12, row = 0)
    Label(frame, text=f"Rented \nBook ID", width = 15, font = ("Barlow", 8, "bold")).pack()

    for i in range(13):
        for j in result:
            l1.append(j[i])

        max = len(l1)

        for k in range(max):
            frame = Frame(win, relief = RAISED, borderwidth = 1)
            frame.grid(column = i, row = k+1)
            Label(frame, text = l1[k], width = 15, font = ("Barlow", 8)).pack()

        l1.clear()

    win.mainloop()