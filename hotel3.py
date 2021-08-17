from tkinter import*
from PIL import Image,ImageTk
from customer import cust_win
from room import RoomBooking


class HotelManagementSystem:
    def __init__(self,root):
      self.root=root
      self.root.title("Hotel Management System")
      self.root.geometry("1550x800+0+0")


      img1=Image.open(r"C:\Users\LENOVO\Desktop\pictures\img2.jpg")
      img1=img1.resize((1550,140),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)
      

      lblimg1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
      lblimg1.place(x=0,y=0,width=1550,height=140)

      img2=Image.open(r"C:\Users\LENOVO\Desktop\pictures\images.png")
      img2=img2.resize((230,140),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)
      

      lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
      lblimg.place(x=0,y=0,width=230,height=140)


    

      lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      lbl_title.place(x=0,y=140,width=1550,height=50)
      
      main_frame=Frame(self.root,bd=4,relief=RIDGE)
      main_frame.place(x=0,y=190,width=1550,height=620)
      
      lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      
      lbl_menu.place(x=0,y=0,width=230)
      
      btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
      btn_frame.place(x=0,y=35,width=228,height=90)

      cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
      cust_btn.grid(row=0,column=0,pady=2)


      room_btn1=Button(btn_frame,text="ROOM",command=self.roombooking,font=("times new roman",14,"bold"),width=22,bg="black",fg="gold",bd=0,cursor="hand1")
      room_btn1.grid(row=1,column=0,pady=2)
      
      

      img3=Image.open(r"C:\Users\LENOVO\Desktop\pictures\img.jpg")
      img3=img3.resize((1310,590),Image.ANTIALIAS)
      self.photoimg3=ImageTk.PhotoImage(img3)
      

      lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
      lblimg1.place(x=225,y=0,width=1310,height=590)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

