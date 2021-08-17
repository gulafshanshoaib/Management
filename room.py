from tkinter import*
#from tkinter.font import Font  
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class RoomBooking:
    def __init__(self,root):
      self.root=root
      self.root.title("Hotel Management System")
      self.root.geometry("1150x550+220+200")
       
      #****************variable*******
      self.var_contact=StringVar()
      self.var_checkin=StringVar()
      self.var_checkout=StringVar()
      self.var_roomtype=StringVar()
      self.var_roomavailable=StringVar()
      self.var_listofitems=StringVar()



      lbl_title=Label(self.root,text="ROOM BOOKING DETAIL",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      lbl_title.place(x=0,y=0,width=1100,height=50)


      img2=Image.open(r"C:\Users\LENOVO\Desktop\pictures\images.png")
      img2=img2.resize((100,40),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)
      
      lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
      lblimg.place(x=5,y=2,width=100,height=40)


      labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Detail",font=("timee new roman",12,"bold"),padx=2)
      labelframeleft.place(x=5,y=50,width=425,height=490)





      lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lbl_cust_contact.grid(row=0,column=0,sticky=W)
      enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("timee new roman",13,"bold"),width=20)
      enty_contact.grid(row=0,column=1)
       
      btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("time new roman",8,"bold"),bg="black",fg="gold",width=8)
      btnFetchData.place(x=350,y=4)

      Check_in_date=Label(labelframeleft,text="Check_In Date",font=("time new roman",12,"bold"),padx=2,pady=6)
      Check_in_date.grid(row=1,column=0,sticky=W)
      txtCheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("timee new roman",13,"bold"),width=29)
      txtCheck_in_date.grid(row=1,column=1)
                          
      Check_out_date=Label(labelframeleft,text="Check_Out Date",font=("time new roman",12,"bold"),padx=2,pady=6)
      Check_out_date.grid(row=2,column=0,sticky=W)
      txtCheck_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("timee new roman",13,"bold"),width=29)
      txtCheck_out_date.grid(row=2,column=1)

      





      label_room_type=Label(labelframeleft,text="Room type",font=("timee new roman",12,"bold"),padx=2,pady=6)
      label_room_type.grid(row=5,column=0,sticky=W)
      combo_room_type=ttk.Combobox(labelframeleft,font=("time new roman",12,"bold"),width=27,state="readonly")   
  
      combo_room_type["value"]=("Single","Double","Laxary")
      combo_room_type.current(0)
      combo_room_type.grid(row=3,column=1)
      


      lbl_RoomAvailable=Label(labelframeleft,text="Room Available",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lbl_RoomAvailable.grid(row=4,column=0,sticky=W)
      txt_RoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("timee new roman",13,"bold"),width=29)
      txt_RoomAvailable.grid(row=4,column=1)

      lst_of_items=Label(labelframeleft,text="List Of Items",font=("timee new roman",12,"bold"),padx=2,pady=6)
      lst_of_items.grid(row=3,column=0,sticky=W)
      txtitems=ttk.Entry(labelframeleft,textvariable=self.var_listofitems,font=("timee new roman",13,"bold"),width=29)
      txtitems.grid(row=3,column=1)

      combo_listofitmes=ttk.Combobox(labelframeleft,font=("time new roman",12,"bold"),width=27,state="readonly")      
      combo_listofitmes["value"]=("TV","Couch","Table","Air Condition","Kitchen Applience")
      combo_listofitmes.current(0)
      combo_listofitmes.grid(row=3,column=1)

      

      
      
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
      
      img2=Image.open(r"C:\Users\LENOVO\Desktop\pictures\img4.jfif")
      img2=img2.resize((150,40),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)
      
      lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
      lblimg.place(x=5,y=2,width=100,height=40)
      
      img3=Image.open(r"C:\Users\LENOVO\Desktop\pictures\img6.jpg")
      img3=img3.resize((520,300),Image.ANTIALIAS)
      self.photoimg3=ImageTk.PhotoImage(img3)
      
      lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
      lblimg.place(x=760,y=55,width=520,height=200)




    
      Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Detail And Search System",font=("timee new roman",12,"bold"),padx=2)
      Table_Frame.place(x=435,y=200,width=860,height=260)
      
      lblSeachBy=Label(Table_Frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
      lblSeachBy.grid(row=0,column=0,sticky=W,padx=2)

      self.serch_var=StringVar()
      combo_Search=ttk.Combobox(Table_Frame,font=("time new roman",12,"bold"),width=18,state="readonly")      
      combo_Search["value"]=("Contact","Room")
      combo_Search.current(0)
      combo_Search.grid(row=0,column=1,padx=2)
      
      self.txt_search=StringVar()
      txt_Search=ttk.Entry(Table_Frame,font=("timee new roman",13,"bold"),width=24)
      txt_Search.grid(row=0,column=2,padx=2)


      btnSearch=Button(Table_Frame,text="Search",font=("time new roman",11,"bold"),bg="black",fg="gold",width=10)
      btnSearch.grid(row=0,column=3,padx=1)
      btnShowAll=Button(Table_Frame,text="Show All",font=("time new roman",11,"bold"),bg="black",fg="gold",width=10)
      btnShowAll.grid(row=0,column=4,padx=1)


      details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
      details_table.place(x=0,y=50,width=720,height=180)

      scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

      self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","listofitems"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      scroll_x.config(command=self.room_table.xview)
      scroll_y.config(command=self.room_table.yview)

      self.room_table.heading("contact",text="Contact")
      self.room_table.heading("checkin",text="Checkin")
      self.room_table.heading("checkout",text="Checkout")
      self.room_table.heading("roomtype",text="Roomtype")
      self.room_table.heading("roomavailable",text="Roomavailable")
      self.room_table.heading("listofitems",text="Listofitems")

      
      self.room_table["show"]="headings"
      
      
      self.room_table.column("contact",width=100)
      self.room_table.column("checkin",width=100)
      self.room_table.column("checkout",width=100)      
      self.room_table.column("roomtype",width=100)
      self.room_table.column("roomavailable",width=100)
      self.room_table.column("listofitems",width=100)
      self.room_table.pack(fill=BOTH,expand=1)
      self.fetch_data()


     
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s)",(
                                                                self.var_contact.get(),
                                                                self.var_checkin.get(),
                                                                self.var_checkout.get(),
                                                                self.var_roomtype.get(),
                                                                self.var_roomavailable.get(),
                                                                self.var_listofitems.get()
                                                                
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
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()  




    def Fetch_contact(self):

      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
        my_cursor=conn.cursor()
        query=("select Name from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        if row==None:
          messagebox.showerror("Error","This number not found",parent=self.root)
        else:
          conn.commit()
          conn.close()
          showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
          showDataframe.place(x=455,y=55,width=300,height=140)


          lblName=Label(showDataframe,text="Name:",font=("time in roman",12,"bold"))
          lblName.place(x=0,y=0)

          lbl=Label(showDataframe,text=row,font=("time in roman",12,"bold"))
          lbl.place(x=90,y=0)


          conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
          my_cursor=conn.cursor()
          query=("select Gender from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          lblGender=Label(showDataframe,text="Gender",font=("time in roman",12,"bold"))
          lblGender.place(x=0,y=30)

          lbl2=Label(showDataframe,text=row,font=("time in roman",12,"bold"))
          lbl2.place(x=90,y=30)

          conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
          my_cursor=conn.cursor()
          query=("select Email from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          lblEmail=Label(showDataframe,text="Email",font=("time in roman",12,"bold"))
          lblEmail.place(x=0,y=60)

          lblEmail=Label(showDataframe,text=row,font=("time in roman",12,"bold"))
          lblEmail.place(x=90,y=60)
          
          conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="management")
          my_cursor=conn.cursor()
          query=("select Address from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          lblGender=Label(showDataframe,text="Address",font=("time in roman",12,"bold"))
          lblGender.place(x=0,y=90)

          lblAddress=Label(showDataframe,text=row,font=("time in roman",12,"bold"))
          lblAddress.place(x=90,y=90)






if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()