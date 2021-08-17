from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class cust_win:
    def __init__(self,root):
      self.root=root
      self.root.title("Hotel Management System")
      self.root.geometry("1185x550+220+210")

      #******************variable************

      self.var_ref=StringVar()
      x=random.randint(1000,9999)
      self.var_ref.set(str(x))


      self.var_cust_name=StringVar()
      self.var_mother=StringVar()
      self.var_gender=StringVar()
      self.var_post=StringVar()
      self.var_mobile=StringVar()
      self.var_email=StringVar()
      self.var_address=StringVar()




      #***********************title*****************
      
      lbl_title=Label(self.root,text="ADD CUSTOMER DETAIL",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      lbl_title.place(x=0,y=0,width=1195,height=50)
      
      #*********************LOGO*****************

      img2=Image.open(r"C:\Users\LENOVO\Desktop\pictures\images.png")
      img2=img2.resize((100,40),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)
      
      lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
      lblimg.place(x=5,y=2,width=100,height=40)

      #***********************LABELFRAME******************

      labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAIL",font=("timee new roman",12,"bold"),padx=2)
      labelframeleft.place(x=5,y=50,width=425,height=490)
      
      #***********************LABELS AND ENTRY**********

      lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lbl_cust_ref.grid(row=0,column=0,sticky=W)
      enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("timee new roman",13,"bold"),width=29,state="readonly")
      enty_ref.grid(row=0,column=1)

      cname=Label(labelframeleft,text="Customer NAME",font=("timee new roman",12,"bold"),padx=2,pady=6)
      cname.grid(row=1,column=0,sticky=W)
      txtcname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("timee new roman",13,"bold"))
      txtcname.grid(row=1,column=1)

      lblmname=Label(labelframeleft,text="MOTHER NAME",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lblmname.grid(row=2,column=0,sticky=W)
      txtmname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mother,font=("timee new roman",13,"bold"))
      txtmname.grid(row=2,column=1)


      label_gender=Label(labelframeleft,text="GENDER",font=("time new roman",12,"bold"),padx=2,pady=6)
      label_gender.grid(row=3,column=0,sticky=W)

      combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("time new roman",12,"bold"),width=27,state="readonly")      
      combo_gender["value"]=("Male","Female","Other")
      combo_gender.current(0)
      combo_gender.grid(row=3,column=1)
      
      lblpostcode=Label(labelframeleft,text="POST CODE",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lblpostcode.grid(row=4,column=0,sticky=W)
      txtpostcode=ttk.Entry(labelframeleft,width=29,textvariable=self.var_post,font=("timee new roman",13,"bold"))
      txtpostcode.grid(row=4,column=1)


      lblmobile=Label(labelframeleft,text="MOBILE NUMBER",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lblmobile.grid(row=5,column=0,sticky=W)
      txtmobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("timee new roman",13,"bold"))
      txtmobile.grid(row=5,column=1)

      lblemail=Label(labelframeleft,text="EMAIL ADDRESS",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lblemail.grid(row=6,column=0,sticky=W)
      txtemail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("timee new roman",13,"bold"))
      txtemail.grid(row=6,column=1)
      
      
      lbladdress=Label(labelframeleft,text="ADDRESS",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lbladdress.grid(row=7,column=0,sticky=W)
      txtaddress=ttk.Entry(labelframeleft,width=29,textvariable=self.var_address,font=("timee new roman",13,"bold"))
      txtaddress.grid(row=7,column=1)
      #********************frame********************
      btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
      btn_frame.place(x=0,y=300,width=412,height=40)

      btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("time new roman",11,"bold"),bg="black",fg="gold",width=10)
      btnAdd.grid(row=0,column=0,padx=1)

      btnupdate=Button(btn_frame,text="Update",font=("time new roman",11,"bold"),bg="black",fg="gold",width=10)
      btnupdate.grid(row=0,column=1,padx=1)
      
      btnDelet=Button(btn_frame,text="Delete",font=("time new roman",11,"bold"),bg="black",fg="gold",width=10)
      btnDelet.grid(row=0,column=2,padx=1)
      
      btnReset=Button(btn_frame,text="Reset",font=("timee new roman",11,"bold"),bg="black",fg="gold",width=10)
      btnReset.grid(row=0,column=3,padx=1)

    
     #***************************TABLE FRAME*************
     
    
      Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Detail And Search System",font=("timee new roman",12,"bold"),padx=2)
      Table_Frame.place(x=435,y=50,width=860,height=490)
      
      lblSeachBy=Label(Table_Frame,font=("time new roman",12,"bold"),text="Search By:",bg="red",fg="white")
      lblSeachBy.grid(row=0,column=0,sticky=W,padx=2)

      
      combo_Search=ttk.Combobox(Table_Frame,font=("time new roman",10,"bold"),width=24,state="readonly")      
      combo_Search["value"]=("MOBILE","REF")
      combo_Search.current(0)
      combo_Search.grid(row=0,column=1,padx=2)

      
      
      txtSearch=ttk.Entry(Table_Frame,font=("timee new roman",13,"bold"),width=24)
      txtSearch.grid(row=0,column=2,padx=2)


      btnSearch=Button(Table_Frame,text="Search",font=("time new roman",10,"bold"),bg="black",fg="gold",width=10)
      btnSearch.grid(row=0,column=3,padx=1)
      btnShowAll=Button(Table_Frame,text="Show All",font=("time new roman",10,"bold"),bg="black",fg="gold",width=10)
      btnShowAll.grid(row=0,column=4,padx=1)

      #************show data table***************

      details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
      details_table.place(x=0,y=50,width=860,height=350)
       
      scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

      self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      
      
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      scroll_x.config(command=self.Cust_Details_Table.xview)
      scroll_y.config(command=self.Cust_Details_Table.yview)

      self.Cust_Details_Table.heading("ref",text="Ref No")
      self.Cust_Details_Table.heading("name",text="Name")
      self.Cust_Details_Table.heading("mother",text="Mother Name")
      self.Cust_Details_Table.heading("gender",text="Gender")
      self.Cust_Details_Table.heading("post",text="PostCode")
      self.Cust_Details_Table.heading("mobile",text="Mobile")
      self.Cust_Details_Table.heading("email",text="Email")
      self.Cust_Details_Table.heading("address",text="Address")
      
      self.Cust_Details_Table["show"]="headings"

      self.Cust_Details_Table.column("ref",width=100)
      self.Cust_Details_Table.column("name",width=100)
      self.Cust_Details_Table.column("mother",width=100)
      self.Cust_Details_Table.column("gender",width=100)
      self.Cust_Details_Table.column("post",width=100)
      self.Cust_Details_Table.column("mobile",width=100)
      self.Cust_Details_Table.column("email",width=100)
      self.Cust_Details_Table.column("address",width=100)



      self.Cust_Details_Table.pack(fill=BOTH,expand=1)
      self.fetch_data()
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_ref.get(),
                                                                self.var_cust_name.get(),
                                                                self.var_mother.get(),
                                                                self.var_gender.get(),
                                                                self.var_post.get(),
                                                                self.var_mobile.get(),
                                                                self.var_email.get(),
                                                                self.var_address.get()
                                                             ))
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
               messagebox.showwarning("warning",f"Somethng went wrong:{str(es)}",parent=self.root) 

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()  
                
if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()