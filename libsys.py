from tkinter import*
from tkinter import ttk

import mysql.connector 

from tkinter import messagebox
import datetime

import tkinter

class LibraryManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # Variables

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        lbltitle=Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd="20", relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # Left Data Frame

        DataFrameLeft=LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd="20", relief=RIDGE, font=("times new roman", 12, "bold") )
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        
        labelMember=Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        labelMember.grid(row=0, column=0, sticky=W)
        comMember=ttk.Combobox(DataFrameLeft, textvar= self.member_var , font=("times new roman", 15, "bold"), width=27, state="readonly")
        comMember["value"]=("Admib STaff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        
        labelPRN=Label(DataFrameLeft, bg="powder blue", text="PRN NO.", font=("times new roman", 15, "bold"), padx=2, pady=4)
        labelPRN.grid(row=1, column=0, sticky=W)
        txtPRN=Entry(DataFrameLeft, textvar=self.prn_var,font=("times new roman", 15, "bold"), width=29 )
        txtPRN.grid(row=1, column=1)


        lblTitle=Label(DataFrameLeft, bg="powder blue", text="Title", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle=Entry(DataFrameLeft, textvar=self.id_var,font=("times new roman", 15, "bold"), width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName=Label(DataFrameLeft, bg="powder blue", text="First Name", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName=Entry(DataFrameLeft, textvar=self.firstname_var,font=("times new roman", 15, "bold"), width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName=Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblLastName.grid(row=4, column=0, sticky=W)
        lblLastName=Entry(DataFrameLeft, textvar=self.lastname_var,font=("times new roman", 15, "bold"), width=29)
        lblLastName.grid(row=4, column=1)

        lblAddress1=Label(DataFrameLeft, bg="powder blue", text="Address 1", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblAddress1.grid(row=5, column=0, sticky=W)
        lblAddress1=Entry(DataFrameLeft, textvar=self.address1_var,font=("times new roman", 15, "bold"), width=29)
        lblAddress1.grid(row=5, column=1)

        lblAddress2=Label(DataFrameLeft, bg="powder blue", text="Address 2", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblAddress2.grid(row=6, column=0, sticky=W)
        lblAddress2=Entry(DataFrameLeft, textvar=self.address2_var,font=("times new roman", 15, "bold"), width=29)
        lblAddress2.grid(row=6, column=1)

        lblPostCode=Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblPostCode.grid(row=7, column=0, sticky=W)
        lblPostCode=Entry(DataFrameLeft, textvar=self.postcode_var,font=("times new roman", 15, "bold"), width=29)
        lblPostCode.grid(row=7, column=1)

        lblMobile=Label(DataFrameLeft, bg="powder blue", text="Mobile", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblMobile.grid(row=8, column=0, sticky=W)
        lblMobile=Entry(DataFrameLeft, textvar=self.mobile_var,font=("times new roman", 15, "bold"), width=29)
        lblMobile.grid(row=8, column=1)

        lblBookId=Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblBookId.grid(row=0, column=2, sticky=W)
        lblBookId=Entry(DataFrameLeft, textvar=self.bookid_var,font=("times new roman", 15, "bold"), width=29)
        lblBookId.grid(row=0, column=3)

        lblBookTitle=Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        lblBookTitle=Entry(DataFrameLeft, textvar=self.booktitle_var,font=("times new roman", 15, "bold"), width=29)
        lblBookTitle.grid(row=1, column=3)

        lblAuthor=Label(DataFrameLeft, bg="powder blue", text="Author", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblAuthor.grid(row=2, column=2, sticky=W)
        lblAuthor=Entry(DataFrameLeft, textvar=self.author_var,font=("times new roman", 15, "bold"), width=29)
        lblAuthor.grid(row=2, column=3)

        lblDateBorrowed=Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        lblDateBorrowed=Entry(DataFrameLeft, textvar=self.dateborrowed_var,font=("times new roman", 15, "bold"), width=29)
        lblDateBorrowed.grid(row=3, column=3)

        lblDateDue=Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblDateDue.grid(row=4, column=2, sticky=W)
        lblDateDue=Entry(DataFrameLeft, textvar=self.datedue_var,font=("times new roman", 15, "bold"), width=29)
        lblDateDue.grid(row=4, column=3)

        lblDaysOnBook=Label(DataFrameLeft, bg="powder blue", text="Days on Book", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        lblDaysOnBook=Entry(DataFrameLeft, textvar=self.daysonbook_var,font=("times new roman", 15, "bold"), width=29)
        lblDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine=Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        lblLateReturnFine=Entry(DataFrameLeft, textvar=self.latefine_var,font=("times new roman", 15, "bold"), width=29)
        lblLateReturnFine.grid(row=6, column=3)

        lblDateOverDue=Label(DataFrameLeft, bg="powder blue", text="Date overdue", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        lblDateOverDue=Entry(DataFrameLeft, textvar=self.dateoverdue_var,font=("times new roman", 15, "bold"), width=29)
        lblDateOverDue.grid(row=7, column=3)

        lblActualPrice=Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        lblActualPrice=Entry(DataFrameLeft, textvar=self.finalprice_var,font=("times new roman", 15, "bold"), width=29)
        lblActualPrice.grid(row=8, column=3)


        # Right Data Frame

        DataFrameRight=LabelFrame(frame, text="Books Info", bg="powder blue", fg="green", bd="20", relief=RIDGE, font=("times new roman", 12, "bold") )
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.txtBox=Text(DataFrameRight, font=("times new roman", 12, "bold"), width=32, height=16, padx=2, pady=6 )
        self.txtBox.grid(row=0, column=2)

        

        listBooks=['Head First Book', 'Learn Python the hard way', 'Python Programming', 'Secret Rahshy', 'Python Cookbook', 'Intro to machine Learning',
                 'Machine Techno', 'My Python', 'Joss Ellif Guru', 'Elite Jungle Python', 'Jungli Python', 'Mumbai Python', 'Pune Python', 'Machine Python', 'Advance Python', 'Inton Python', 'Redchilli Python', 'Ishq Python' ]
        
        def SelectBook(event=""):
            val=str(listBox.get(listBox.curselection()))
            x=val
            if(x=="Head First Book"):
                self.bookid_var.set("BKID123")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("John Doe")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 788")

            elif(x=="Learn Python the hard way"):
                self.bookid_var.set("BKID124")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Brad Pitt")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs 100")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 1000")

            elif(x=="Python Programming"):
                self.bookid_var.set("BKID200")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Leo Messi")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs 150")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 1200")

            elif(x=="Secret Rahshy"):
                self.bookid_var.set("BKID400")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Krishna")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs 204")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 1230")

            elif(x=="Python Cookbook"):
                self.bookid_var.set("BKID500")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Dev Hudson")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs 300")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 1400")


        listBox=Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)

        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky="ns")
        listScrollBar.config(command=listBox.yview)

        for i in listBooks:
            listBox.insert(END, i)

        # Button Frames

        buttonframe = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        buttonframe.place(x=0, y=530, width=1530, height=70)        

        

        #Buttons

        btnAddData=Button(buttonframe, text="Add Data", command=self.add_data, font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData=Button(buttonframe, text="Show Data",command=self.show_data, font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate=Button(buttonframe, text="Update", command=self.update_data, font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnDelete=Button(buttonframe, text="Delete", command=self.delete_data, font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3)

        btnReset=Button(buttonframe, text="Reset",command=self.reset, font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnReset.grid(row=0, column=4)

        btnExit=Button(buttonframe, command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnExit.grid(row=0, column=5)

        # Info Frame

        infoframe = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        infoframe.place(x=0, y=600, width=1530, height=190)

        Table_frame=Frame(infoframe, bd=6, relief="ridge", bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=165)

        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)          


        self.library_table=ttk.Treeview(Table_frame, column=("membertype", "prnno", "title", "firstname", "lastname", "address1",
                                                             "address2", "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed",
                                                             "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set )

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Overdue")
        self.library_table.heading("finalprice", text="Final Price")
        

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        

        

       # self.library_table= ttk.Treeview(Table_frame, xscrollcommand=xscroll.set)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="9825500559@zil", database="proj")
        cursor=conn.cursor()
        cursor.execute("insert into libsys values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get()          
                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Member has been added successfully")


    def update_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="9825500559@zil", database="proj")
        cursor=conn.cursor()
        cursor.execute("update libsys set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostID=%s, Mobile=%s, Bookid=%s, booktitle=%s, Author=%s, Dateborrowed=%s, datedue=%s, daysofbook=%s, latereturnfine=%s, dateoverdue=%s, finalprice=%s where PRN_NO=%s",(
                                                                                                    self.member_var.get(), 
                                                                                                    self.id_var.get(),
                                                                                                    self.firstname_var.get(),
                                                                                                    self.lastname_var.get(),
                                                                                                    self.address1_var.get(),
                                                                                                    self.address2_var.get(),
                                                                                                    self.postcode_var.get(),
                                                                                                    self.mobile_var.get(),
                                                                                                    self.bookid_var.get(),
                                                                                                    self.booktitle_var.get(),
                                                                                                    self.author_var.get(),
                                                                                                    self.dateborrowed_var.get(),
                                                                                                    self.datedue_var.get(),
                                                                                                    self.daysonbook_var.get(),
                                                                                                    self.latefine_var.get(),
                                                                                                    self.dateoverdue_var.get(),
                                                                                                    self.finalprice_var.get(),
                                                                                                    self.prn_var.get()                                                                                                                                     
                                                                                                ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Member has been updated.")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="9825500559@zil", database="proj")
        cursor=conn.cursor()
        cursor.execute("select * from libsys")
        rows=cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)

            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])        
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latefine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])


    def show_data(self):
        self.txtBox.insert(END, "Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No.:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No. :\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END, "FIrstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address 1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address 2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No.\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Days On Book\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "LateRetFine\t\t"+ self.latefine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverdue\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "FinalPrice\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")        
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latefine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System", "Do you want to quit?")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete_data(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error", "Member not selected.")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="9825500559@zil", database="proj")
            cursor=conn.cursor()
            query="delete from libsys where PRN_NO=%s"
            value=(self.prn_var.get(),)
            cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been deleted")



if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()