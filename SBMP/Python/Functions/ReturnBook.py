from tkinter import *
from tkinter import messagebox
from mysql.connector import *
from Functions.RenterList import *

def rtnbkdb():

    transID = int(rtnbkInfo.get())

    allBk = []
    qrbkid = []
    qrresult = []
    qravlbqty = []

    extractbk = "SELECT transac_num FROM book_rent_master;"
    try:
        cur.execute(extractbk)
        result = cur.fetchall()

        for i in result:
            allBk.append(i[0])

        if transID in allBk:
            checkQuery = f"SELECT rent_status FROM book_rent_master WHERE transac_num={transID};"
            cur.execute(checkQuery)
            result = cur.fetchall()
            for i in result:
                qrresult.append(i[0])

            getbkID = f"SELECT book_id FROM book_rent_master where transac_num={transID};"
            cur.execute(getbkID)
            bkid = cur.fetchall()
            for i in bkid:
                qrbkid.append(i[0])

            getavlbqty = f"SELECT book_avlb_qty FROM book_list_master WHERE book_id={qrbkid[0]};"
            cur.execute(getavlbqty)
            avlbqty = cur.fetchall()
            for i in avlbqty:
                qravlbqty.append(i[0])

            qty = qravlbqty[0]
            qty +=1

            if qrresult[0] == 1:
                finalQuery = f"UPDATE book_rent_master SET rent_status=0, return_date=current_timestamp() WHERE transac_num={transID};"
                updtval = f"UPDATE book_list_master SET book_avlb_qty={qty} WHERE book_id={qrbkid[0]};"
                cur.execute(finalQuery)
                con.commit()
                cur.execute(updtval)
                con.commit()

                messagebox.showinfo("Successful", "Book returned succesfully")
            else:
                messagebox.showinfo("Already returned", "Book already returned")
    except:
        messagebox.showinfo("Error", "Some error has been occurred")
    finally:
        allBk.clear()
        qrbkid.clear()
        qrresult.clear()
        qravlbqty.clear()

    win.destroy()

def op():
    global win, con, cur, rtnbkInfo

    # Adding database details
    con = connect(host = "localhost", user = "root", password = "", database = "lib_mgmt_sys")
    cur = con.cursor()

    # Creating a window
    win = Tk()
    win.title("Library Management System - Return Book")
    win.geometry("800x480")
    win.minsize(width = 800, height = 480)

    # Creating a title and menu frame
    titleFrame = Frame(win, bg = "#005B96")
    titleFrame.place(relx = 0.0, rely = 0.0, relwidth = 1.0, relheight = 0.15)

    menuFrame = Frame(win, bg = "#6497B1")
    menuFrame.place(relx = 0.0, rely = 0.15, relwidth = 1.0, relheight = 0.85)

    # Creating a title heading
    heading = Label(titleFrame, text = "Return Book", font = ("Barlow", 20, "bold"), bg = "#005B96", fg = "white")
    heading.place(relx = 0.50, rely = 0.50, anchor = CENTER)

    # Creating a form
    rtnbk = Label(menuFrame, text = "Transaction ID: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    rtnbk.place(relx = 0.40, rely = 0.10, anchor = CENTER)
    rtnbkInfo = Entry(menuFrame)
    rtnbkInfo.place(relx = 0.60, rely = 0.10, anchor = CENTER)

    RenterList = Button(menuFrame, text = "Renter's List", font = ("Barlow", 10), command = rntslist)
    RenterList.place(relx = 0.40, rely = 0.25, anchor = CENTER)

    SubmitBtn = Button(menuFrame, text = "Return Book", font = ("Barlow", 10), command = rtnbkdb)
    SubmitBtn.place(relx = 0.60, rely = 0.25, anchor = CENTER)

    win.mainloop()    