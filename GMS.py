#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter import *
from tkcalendar import *
from PIL import ImageTk,Image

def date():
    app=Toplevel(root)
    app.geometry("2000x1000")
    app.title("Appointment")
    app.rowconfigure(0,weight=1)
    app.columnconfigure(0,weight=1)
    Frame(app,bg="linen").grid(row=0,column=0,sticky="nsew")
    title=Label(app,text="Appointment",font=("Comic Sans MS",40,"bold"),bg="red",fg="yellow",relief='raised',).place(x=0,y=0,relwidth=1)  
    var=StringVar()  
    msg=Message(app,text="Yoga classes from 10:30-12:30",font=("times new roman",50,"bold"),fg='red').place(x=450,y=200)

def calendar():
    table=Toplevel(root)
    table.geometry("2000x1000")
    table.title("Time Table")
    table.rowconfigure(0,weight=1)
    table.columnconfigure(0,weight=1)
    Frame(table,bg="linen").grid(row=0,column=0,sticky="nsew")
    title=Label(table,text="Calendar",font=("Comic Sans MS",40,"bold"),bg="red",fg="yellow",relief='raised',).place(x=0,y=0,relwidth=1)   
    cal=Calendar(table,selectmode='day',year=2020,month=10,day=22).place(x=500,y=200)
    b1=Button(table,text='Get Appointment',width=20,font=("times new roman",13,"bold"),bg="red",fg="white",command=date).place(x=520,y=400)
    
    
    
def done():
    success=Toplevel(root)
    success.geometry("2000x1000")
    success.title("Status")
    var=StringVar()  
    msg=Message(success,text="Payment is successful",font=("times new roman",50,"bold"),fg='red').place(x=450,y=200)    
    
    
def payment():
    pay=Toplevel(root)
    pay.geometry("2000x1000")
    pay.title("Payment")
    pay.rowconfigure(0,weight=1)
    pay.columnconfigure(0,weight=1)
    Frame(pay,bg="linen").grid(row=0,column=0,sticky="nsew")
    title=Label(pay,text="Payment",font=("Comic Sans MS",40,"bold"),bg="red",fg="yellow",relief='raised',).place(x=0,y=0,relwidth=1)   
    email=StringVar()
    branch=StringVar()
    card=StringVar()
    cvv=StringVar()
    amt=StringVar()
   
    lblem=Label(pay,text="E-Mail",height=0,font=("times new roman",20,"bold")).place(x=330,y=200)
    txtem=Entry(pay,textvariable=email,bd=5,width=25,font=("",15)).place(x=600,y=200)     
    lblbranch=Label(pay,text="Branch",height=0,font=("times new roman",20,"bold")).place(x=330,y=250)
    txtbranch=Entry(pay,textvariable=branch,bd=5,width=25,font=("",15)).place(x=600,y=250)
    lblcard=Label(pay,text="Card No",height=0,font=("times new roman",20,"bold")).place(x=330,y=300)
    txtcard=Entry(pay,textvariable=card,show="*",bd=5,width=25,font=("",15)).place(x=600,y=300) 
    lblcvv=Label(pay,text="CVV",height=0,font=("times new roman",20,"bold")).place(x=330,y=350)
    txtcvv=Entry(pay,textvariable=cvv,bd=5,width=25,font=("",15)).place(x=600,y=350)
    lblamt=Label(pay,text="Amount",height=0,font=("times new roman",20,"bold")).place(x=330,y=400)
    txtamt=Entry(pay,textvariable=amt,bd=5,width=25,font=("",15)).place(x=600,y=400)
    btn_login=Button(pay,text="PAY >>",width=20,font=("times new roman",20,"bold"),bg="red",fg="white",command=done).place(x=450,y=500)
        

def membership():
    member=Toplevel(root)
    member.geometry("2000x1000")
    member.title("Membership")
    member.rowconfigure(0,weight=1)
    member.columnconfigure(0,weight=1)
    Frame(member,bg="palegreen").grid(row=0,column=0,sticky="nsew")
    title=Label(member,text="Membership Offers",font=("Comic Sans MS",40,"bold"),bg="red",fg="yellow",relief='raised',).place(x=0,y=0,relwidth=1) 
    b1=Button(member,text = "Diamond \n Rs 1500/month",font=("times new roman",20,"bold"),width=20,height=10,bg="cyan",command=payment).place(x=70,y=220)
    b2=Button(member,text = "Gold \n Rs 900/month",font=("times new roman",20,"bold"),width=20,height=10,bg="gold",command=payment).place(x=470,y=220)
    b3=Button(member,text = "Silver \n Rs 500/month",font=("times new roman",20,"bold"),width=20,height=10,bg="thistle1",command=payment).place(x=870,y=220)
   
    
def notice():
    note=Toplevel(root)
    note.geometry("2000x1000")
    note.title("Notice")
    notice1=Label(note,text="NOTICE",font=("Comic Sans MS",40,"bold"),bg="red",fg="yellow",relief='raised',).place(x=0,y=0,relwidth=1) 
    var=StringVar()  
    msg=Message(note,text="Tommorow is Holiday!",font=("times new roman",50,"bold"),fg='black').place(x=400,y=250)    
     
    
    
def dashboard():
    main=Toplevel(root)
    main.geometry("2000x1000")
    main.title("Dashboard") 
    main.rowconfigure(0,weight=1)
    main.columnconfigure(0,weight=1)
    Frame(main,bg="linen").grid(row=0,column=0,sticky="nsew")
    title=Label(main,text="Dashboard",font=("Comic Sans MS",30,"bold"),bg="red",fg="yellow",relief='raised',).place(x=0,y=0,relwidth=1)   
    b1=Button(main,text = "Calendar",width=20,height=7,bg="orange",font=("times new roman",20,"bold"),command=calendar).place(x=190,y=90)
    b2=Button(main,text = "Payment",width=20,height=7,bg="orange",font=("times new roman",20,"bold"),command=payment).place(x=700,y=90)
    b3=Button(main,text = "Membership",width=20,height=7,bg="orange",font=("times new roman",20,"bold"),command=membership).place(x=190,y=400)
    b4=Button(main,text = "Notice",width=20,height=7,bg="orange",font=("times new roman",20,"bold"),command=notice).place(x=700,y=400)

def login():
    new=Toplevel(root)
    new.geometry("2000x1000")
    new.title("LogIn Page")
    new.rowconfigure(0,weight=1)
    new.columnconfigure(0,weight=1)
    Frame(new,bg="linen").grid(row=0,column=0,sticky="nsew")
    title=Label(new,text="Have A Healthy Day Ahead !",font=("Comic Sans MS",40,"bold"),bg="red",fg="yellow",relief='raised',).place(x=0,y=0,relwidth=1)   
    user=StringVar()
    passw=StringVar()
    lbluser=Label(new,text="USERNAME",height=0,font=("times new roman",20,"bold")).place(x=300,y=200)
    txtuser=Entry(new,textvariable=user,bd=5,width=25,font=("",15)).place(x=600,y=200)
    lblpass=Label(new,text="GYM ID",height=0,font=("times new roman",20,"bold")).place(x=300,y=250)
    txtpass=Entry(new,textvariable=passw,show="*",bd=5,width=25,font=("",15)).place(x=600,y=250)     
    btn_login=Button(new,text="Hit The Gym >>",width=20,font=("times new roman",20,"bold"),bg="red",fg="white",command=dashboard).place(x=450,y=450)
        

root=Tk()
root.geometry("2000x1000")
root.title('Gym management system')
i=Image.open(r"C:\Users\atulk\Downloads\pic5.jpg")  
i=i.resize((1500,700), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(i)  
cv = Canvas()  
cv.pack(side='top', fill='both', expand='yes')  
cv.create_image(0, 0, image=photo, anchor='nw')
b=Button(root,text="WELCOME TO THE IRON PARADISE",font=("arial",13,"bold"),relief='raised',bg='red',fg='yellow',activebackground='red',activeforeground='yellow',height=2,width=40,command=login).place(x=770,y=550)
root.mainloop()


# In[ ]:





# In[ ]:




