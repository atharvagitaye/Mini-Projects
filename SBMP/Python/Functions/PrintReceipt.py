from tkinter import *
from tkinter import messagebox
from mysql.connector import *
from fpdf import FPDF
from Functions.RenterList import *

def prtrcpt():

    global success

    qrinfo = []
    rntlst = []
    bknamelt = []

    tid = int(transidInfo.get())

    query = "SELECT transac_num FROM book_rent_master;"
    
    try:
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            qrinfo.append(i[0])

        if tid in qrinfo:
            rntqr = f"SELECT * FROM book_rent_master WHERE transac_num={tid};"

            cur.execute(rntqr)
            result = cur.fetchall()

            for i in result[0]:
                rntlst.append(i)

            bkname = f"SELECT book_name FROM book_list_master WHERE book_id={rntlst[12]};"

            cur.execute(bkname)
            result = cur.fetchall()

            for i in result[0]:
                bknamelt.append(i)

            pdf = FPDF()

            # Add a page
            pdf.add_page()

            # Set the font for the heading
            pdf.set_font("Arial", size = 26, style="B")

            # Write the heading
            pdf.cell(0, 10, "Absolute Minds Library", ln=1, align="C")

            pdf.set_font("Arial", size = 18)
            pdf.cell(0, 10, "Receipt", ln = 1, align = "C")

            # Set the font for the body text
            pdf.set_font("Arial", size=12)

            # Write the body text
            pdf.cell(0, 10, f"Transaction ID: #{rntlst[0]}", ln=1)
            pdf.cell(0, 10, f"Name: {rntlst[1]}", ln=1)
            pdf.cell(0, 10, f"Date and time: {rntlst[3]}", ln=1)
            pdf.cell(0, 10, f"Contact No.: {rntlst[10]}", ln=1)
            pdf.cell(0, 10, f"Email ID: {rntlst[11]}", ln=1)
            pdf.cell(0, 10, f"Book ID: {rntlst[12]}", ln=1)
            pdf.cell(0, 10, f"Book name: {bknamelt[0]}", ln=1)

            # Output the PDF
            pdf.output(f"Receipts/{rntlst[0]} {rntlst[1]}.pdf")

            messagebox.showinfo("Successful", "Receipt generated successfully under Receipt folder")
        else:
            messagebox.showinfo("Error", "Transaction ID not present")

    except:
        messagebox.showinfo("Error", "Some error has been occurred")

    finally:
        qrinfo.clear()
        rntlst.clear()
        bknamelt.clear()
        win.destroy()

def op():

    global con, cur, win, transidInfo

    # Adding database details
    con = connect(host = "localhost", user = "root", password = "", database = "lib_mgmt_sys")
    cur = con.cursor()

    # Creating a window
    win = Tk()
    win.title("Library Management System - Print Receipt")
    win.geometry("800x480")
    win.minsize(width = 800, height = 480)

    # Creating a title and menu frame
    titleFrame = Frame(win, bg = "#005B96")
    titleFrame.place(relx = 0.0, rely = 0.0, relwidth = 1.0, relheight = 0.15)

    menuFrame = Frame(win, bg = "#6497B1")
    menuFrame.place(relx = 0.0, rely = 0.15, relwidth = 1.0, relheight = 0.85)

    # Creating a title heading
    heading = Label(titleFrame, text = "Print Receipt", font = ("Barlow", 20, "bold"), bg = "#005B96", fg = "white")
    heading.place(relx = 0.50, rely = 0.50, anchor = CENTER)

    # Creating a menu
    transid = Label(menuFrame, text = "Transaction ID: ", bg = "#6497B1", fg = "white", font = ("Barlow", 10))
    transid.place(relx = 0.40, rely = 0.10, anchor = CENTER)
    transidInfo = Entry(menuFrame)
    transidInfo.place(relx = 0.60, rely = 0.10, anchor = CENTER)

    RenterList = Button(menuFrame, text = "Renter's List", font = ("Barlow", 10), command = rntslist)
    RenterList.place(relx = 0.40, rely = 0.25, anchor = CENTER)

    SubmitBtn = Button(menuFrame, text = "Print Receipt", font = ("Barlow", 10), command = prtrcpt)
    SubmitBtn.place(relx = 0.60, rely = 0.25, anchor = CENTER)