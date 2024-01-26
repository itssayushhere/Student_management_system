import mysql.connector
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1520x770+0+0")

        title=Label(self.root,text="School Management System",bd=10,relief=GROOVE,font=("Courier",30,"bold"),fg="Black")
        title.pack(side=TOP,fill=X)

#______________Variables______________________________________
        self.Roll_No_Var=StringVar()
        self.Name_Var=StringVar()
        self.Email_Var=StringVar()
        self.Gender_Var=StringVar()
        self.Contact_Var=StringVar()
        self.DOB_Var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

#________________________________ManageFrame____________________________________

        Manage_Frame=Frame(self.root,bd=10,relief=RIDGE,bg="Black")
        Manage_Frame.place(x=20,y=100,width=570,height=650)

        m_title=Label(Manage_Frame,text="Manage Students",font=("Courier",23,"bold"),bg="Black",fg="White")
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_roll=Label(Manage_Frame,text="Roll Number:",font=("Courier",18,"bold"),bg="Black",fg="White")
        lbl_roll.grid(row=1,column=0,pady=20,padx=10,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_Var,font=("Courier",15,"bold"),fg="Black",bd=5,relief=GROOVE,width=20)
        txt_roll.grid(row=1,column=1,padx=5,pady=5,sticky="w")
        
        lbl_name=Label(Manage_Frame,text="Full Name:",font=("Courier",18,"bold"),bg="Black",fg="White")
        lbl_name.grid(row=2,column=0,pady=20,padx=10,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.Name_Var,font=("Courier",15,"bold"),fg="Black",bd=5,relief=GROOVE,width=20)
        txt_name.grid(row=2,column=1,padx=5,pady=5)

        lbl_Email=Label(Manage_Frame,text="Email ID:",font=("Courier",18,"bold"),bg="Black",fg="White")
        lbl_Email.grid(row=3,column=0,pady=20,padx=10,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.Email_Var,font=("Courier",15,"bold"),fg="Black",bd=5,relief=GROOVE,width=20)
        txt_Email.grid(row=3,column=1,padx=5,pady=5,sticky="w")

        lbl_Gender=Label(Manage_Frame,text="Gender:",font=("Courier",18,"bold"),bg="Black",fg="White")
        lbl_Gender.grid(row=4,column=0,pady=20,padx=10,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_Var,font=("Courier",14,"bold"),state='readonly')        
        combo_gender['values']=('Male','Female','Other')
        combo_gender.grid(row=4,column=1,pady=20,padx=10)

        lbl_Contact=Label(Manage_Frame,text="Contact:",font=("Courier",18,"bold"),bg="Black",fg="White")
        lbl_Contact.grid(row=5,column=0,pady=20,padx=10,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.Contact_Var,font=("Courier",15,"bold"),fg="Black",bd=5,relief=GROOVE,width=20)
        txt_Contact.grid(row=5,column=1,padx=5,pady=5,sticky="w")

        lbl_date=Label(Manage_Frame,text="D.O.B:",font=("Courier",18,"bold"),bg="Black",fg="White")
        lbl_date.grid(row=6,column=0,pady=20,padx=10,sticky="w")

        txt_date=Entry(Manage_Frame,textvariable=self.DOB_Var,font=("Courier",15,"bold"),fg="Black",bd=5,relief=GROOVE,width=20)
        txt_date.grid(row=6,column=1,padx=5,pady=5,sticky="w")

        lbl_Address=Label(Manage_Frame,text="Address:",font=("Courier",18,"bold"),bg="Black",fg="White")
        lbl_Address.grid(row=7,column=0,pady=20,padx=10,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=33,height=3,font=("",10),bd=5)
        self.txt_Address.grid(row=7,column=1,pady=20,padx=10,sticky="w")

#__________________________Button_Frame_____________________________________________________________________
        Button_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="Black")
        Button_Frame.place(x=15,y=530,width=510,height=90)

        Add=Button(Button_Frame,text="Add",font=("Arial"),width=10,height=2,command=self.add_students).grid(row=0,column=0,padx=12,pady=13)
        update=Button(Button_Frame,text="Update",command=self.update_data,font=("Arial"),width=10,height=2).grid(row=0,column=1,padx=12,pady=13)
        Delete=Button(Button_Frame,text="Delete",font=("Arial"),width=10,height=2,command=self.delete_data).grid(row=0,column=2,padx=12,pady=13)
        cllear=Button(Button_Frame,text="Clear",font=("Arial"),command=self.clear,width=10,height=2).grid(row=0,column=3,padx=12,pady=13)


#________________________________DetailFrame____________________________________
        
        Detail_Frame=Frame(self.root,bd=10,relief=RIDGE,bg="Black")
        Detail_Frame.place(x=620,y=100,width=900,height=650)

        search_lb=Label(Detail_Frame,text="Search By:",font=("Courier",18,"bold"),bg="Black",fg="White")
        search_lb.grid(row=0,column=0,pady=5,padx=10,sticky="w")

        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("Courier",10,"bold"),state='readonly')        
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,pady=20,padx=10)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("Courier",10,"bold"),fg="Black",bd=2,relief=GROOVE,width=25)
        txt_search.grid(row=0,column=2,padx=5,pady=5,sticky="w")

        search_bt=Button(Detail_Frame,text="Search",command=self.Search_data,font=("Bastion"),width=14,height=1).grid(row=0,column=3,padx=12,pady=12)
        Show_all_bt=Button(Detail_Frame,text="Show all",command=self.fetch_data,font=("Bastion"),width=10,height=1).grid(row=0,column=4,padx=12,pady=12)

#____________________Tabble_frame___________________

        table_frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="Black")
        table_frame.place(x=10,y=70,height=560,width=870)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(table_frame,columns=("Roll","Name","Email","Gender","Contact","D.O.B.","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll no.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("D.O.B.",text="D.O.B.")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("Roll",width=50)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("D.O.B.",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursur)
        self.fetch_data()


#____________________database_____________________________________________
#create mysql databse with your choice and edit in database = '(your database)' and enter your passwd = '(yours)'
#create following column in that database Roll_No , Name ,Email , Gender , Contact , DOB ,txt_Address
    def add_students(self):
        if self.Roll_No_Var.get()==""or self.Name_Var.get()=="":
                messagebox.showerror("Error","ALl fields are required!!!")
        else:        
        
                con=mysql.connector.connect(host="localhost",user="root",passwd="ayushman",database="ayushman")
                cur=con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_Var.get(),
                                                                        self.Name_Var.get(),
                                                                        self.Email_Var.get(),
                                                                        self.Gender_Var.get(),
                                                                        self.Contact_Var.get(),
                                                                        self.DOB_Var.get(),
                                                                        self.txt_Address.get('1.0',END)
                                                                        ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been made")


    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",passwd="ayushman",database="ayushman")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.Roll_No_Var.set("")
        self.Name_Var.set("")
        self.Email_Var.set("")        
        self.Gender_Var.set("")
        self.Contact_Var.set("")
        self.DOB_Var.set("")
        self.txt_Address.delete('1.0',END)

    def get_cursur(self,ev):
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']
        self.Roll_No_Var.set(row[0])
        self.Name_Var.set(row[1])
        self.Email_Var.set(row[2])        
        self.Gender_Var.set(row[3])
        self.Contact_Var.set(row[4])
        self.DOB_Var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])

    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",passwd="ayushman",database="ayushman")
        cur=con.cursor()
        cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where Roll_No=%s",(
                                                                        self.Name_Var.get(),
                                                                        self.Email_Var.get(),
                                                                        self.Gender_Var.get(),
                                                                        self.Contact_Var.get(),
                                                                        self.DOB_Var.get(),
                                                                        self.txt_Address.get('1.0',END),
                                                                        self.Roll_No_Var.get()
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",passwd="ayushman",database="ayushman")
        cur=con.cursor()
        cur.execute("delete from students where Roll_No="+str(self.Roll_No_Var.get()))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def Search_data(self):
        #your data base connection password and database
        con=mysql.connector.connect(host="localhost",user="root",passwd="ayushman",database="ayushman")
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()    


root=Tk()
ob= Student(root)
root.mainloop()
