from tkinter import *
from tkinter import messagebox
from mysql.connector import *
from Functions.ViewBooks import *

def isbkdb(): 
    # List to store books id
    bkid = []
    bkid2 = []
    global bkqtycheck, bkqty
    bkqtycheck = []
    bkqty = 0

    rname = nameInfo.get()
    aInfo = ageInfo.get()
    rtn = rtndateInfo.get()
    addr1 = add1Info.get("1.0", END)
    addr2 = add2Info.get("1.0", END)
    pincode = pncdInfo.get()
    contact = contInfo.get()
    emInfo = emailInfo.get()
    bkInfo = int(bkidInfo.get())

    extractbk = "SELECT book_id FROM book_list_master;"
    try:
        cur.execute(extractbk)
        result = cur.fetchall()

        for i in result:
            bkid.append(i[0])

        if bkInfo in bkid:
            checkAvail = f"SELECT book_status FROM book_list_master WHERE book_id={bkInfo};"
            cur.execute(checkAvail)
            result = cur.fetchall()

            for i in result:
                bkid2.append(i[0])
                
            if bkid2[0] == 1:
                status = True
                bkqty = f"SELECT book_avlb_qty FROM book_list_master where book_id={bkInfo};"
                cur.execute(bkqty)
                result = cur.fetchall()

                for i in result:
                    bkqtycheck.append(i[0])

                bkqty = bkqtycheck[0]
                bkqty -= 1
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issue = f"INSERT INTO `book_rent_master` (`transac_num`, `renter_name`, `renter_age`, `renting_date`, `prm_return_date`, `return_date`, `rent_status`, `address_line1`, `address_line2`, `pincode`, `renter_cont`, `renter_email`, `book_id`) VALUES ('', '{rname}', '{aInfo}', current_timestamp(), '{rtn} 00:00:00', '', '1', '{addr1}', '{addr2}', '{pincode}', '{contact}', '{emInfo}', '{bkInfo}');"
    update = f"UPDATE book_list_master SET book_avlb_qty={bkqty} where book_id={bkInfo}"

    try:
        if bkInfo in bkid and status == True:
            cur.execute(issue)
            con.commit()
            cur.execute(update)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
        else:
            bkid.clear()
            bkid2.clear()
            bkqtycheck.clear()
            messagebox.showinfo('Message', "Book Already Issued")
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")
    finally:
        bkid.clear()
        bkid2.clear()
        bkqtycheck.clear()

    win.destroy()

def op():
    global win, con, cur, nameInfo, ageInfo, rtndateInfo, add1Info, add2Info, pncdInfo, contInfo, emailInfo, bkidInfo

    # Adding database details
    con = connect(host = "localhost", user = "root", password = "", database = "lib_mgmt_sys")
    cur = con.cursor()

    # Creating a window
    win = Tk()
    win.title("Library Management System - Issue Book")
    win.geometry("800x480")
    win.minsize(width = 800, height = 480)

    # Creating a title and menu frame
    titleFrame = Frame(win, bg = "#005B96")
    titleFrame.place(relx = 0.0, rely = 0.0, relwidth = 1.0, relheight = 0.15)

    menuFrame = Frame(win, bg = "#6497B1")
    menuFrame.place(relx = 0.0, rely = 0.15, relwidth = 1.0, relheight = 0.85)

    # Creating a title heading
    heading = Label(titleFrame, text = "Issue Book", font = ("Barlow", 20, "bold"), bg = "#005B96", fg = "white")
    heading.place(relx = 0.50, rely = 0.50, anchor = CENTER)
    
    # Creating a form
    name = Label(menuFrame, text = "Name: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    name.place(relx = 0.40, rely = 0.09, anchor = CENTER)
    nameInfo = Entry(menuFrame)
    nameInfo.place(relx = 0.60, rely = 0.09, anchor = CENTER)

    age = Label(menuFrame, text = "Age: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    age.place(relx = 0.40, rely = 0.18, anchor = CENTER)
    ageInfo = Entry(menuFrame)
    ageInfo.place(relx = 0.60, rely = 0.18, anchor = CENTER)

    rtndate = Label(menuFrame, text = "Promised Return date: \n(yyyy-mm-dd)", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    rtndate.place(relx = 0.40, rely = 0.27, anchor = CENTER)
    rtndateInfo = Entry(menuFrame)
    rtndateInfo.place(relx = 0.60, rely = 0.27, anchor = CENTER)

    add1 = Label(menuFrame, text = "Address Line 1: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    add1.place(relx = 0.40, rely = 0.36, anchor = CENTER)
    add1Info = Text(menuFrame, width = 20, height = 2)
    add1Info.place(relx = 0.60, rely = 0.36, anchor = CENTER)

    add2 = Label(menuFrame, text = "Address Line 2: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    add2.place(relx = 0.40, rely = 0.45, anchor = CENTER)
    add2Info = Text(menuFrame, width = 20, height = 2)
    add2Info.place(relx = 0.60, rely = 0.45, anchor = CENTER)

    pncd = Label(menuFrame, text = "Pincode: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    pncd.place(relx = 0.40, rely = 0.54, anchor = CENTER)
    pncdInfo = Entry(menuFrame)
    pncdInfo.place(relx = 0.60, rely = 0.54, anchor = CENTER)

    cont = Label(menuFrame, text = "Contact No.: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    cont.place(relx = 0.40, rely = 0.63, anchor = CENTER)
    contInfo = Entry(menuFrame)
    contInfo.place(relx = 0.60, rely = 0.63, anchor = CENTER)

    email = Label(menuFrame, text = "Email: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    email.place(relx = 0.40, rely = 0.72, anchor = CENTER)
    emailInfo = Entry(menuFrame)
    emailInfo.place(relx = 0.60, rely = 0.72, anchor = CENTER)

    bkid = Label(menuFrame, text = "Book ID: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    bkid.place(relx = 0.40, rely = 0.81, anchor = CENTER)
    bkidInfo = Entry(menuFrame)
    bkidInfo.place(relx = 0.60, rely = 0.81, anchor = CENTER)

    ViewBooks = Button(menuFrame, text = "View Books", font = ("Barlow", 10), command = viewbk)
    ViewBooks.place(relx = 0.40, rely = 0.95, anchor = CENTER)

    SubmitBtn = Button(menuFrame, text = "Issue Book", font = ("Barlow", 10), command = isbkdb)
    SubmitBtn.place(relx = 0.60, rely = 0.95, anchor = CENTER)

    win.mainloop()