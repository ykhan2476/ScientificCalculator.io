from tkinter import *
import math
 
##methods##
 
def root():
   e1.delete(0,END)
   e1.insert(0,"√")
   global fun
   fun="√"
    
def sin():
    e1.delete(0,END)
    global fun
    fun="sin"
    
def cos():
    e1.delete(0,END)
    global fun
    fun="cos"
    
def tan():
    e1.delete(0,END)
    global fun
    fun="tan"
    
def sini():
    e1.delete(0,END)
    global fun
    fun="sini"
    
def cosi():
    e1.delete(0,END)
    global fun
    fun="cosi"  
    
def tani():
    e1.delete(0,END)
    global fun
    fun="tani"        
   
def rad():
    global n
    n=float(e1.get())
    e1.delete(0,END)
    global fun
    fun="rad"   
    
def log():
    e1.delete(0,END)
    global fun
    fun="log" 
        
def deg():
    global n
    n=float(e1.get())
    e1.delete(0,END)
    global fun
    fun="deg" 
    
def Exp():
    global n
    n=e1.get()
    e1.insert(len(n)+1,"^")
    global fun
    fun="**"
    
 
def sub():
  global n    
  n=e1.get()
  e1.delete(0,END)
  if len(n)==0:
      e1.insert(END,"-")
  else:
      global fun
      fun="-"  
      
def mul():
  global n
  n=float(e1.get())
  e1.delete(0,END)
  global fun
  fun="*"
  
  
def sum():
   global n
   n=float(e1.get())
   e1.delete(0,END)
   global fun
   fun="+"
 
 
def div():
  global n
  n=float(e1.get() )
  e1.delete(0,END)   
  global fun
  fun="/" 
    
def  mod():
  global n
  n=float(e1.get())
  e1.delete(0,END)
  global fun
  fun="%"  
    
def  clear():
    e1.delete(0,END)
 
def bksp():
  e1.delete(len(e1.get())-1,END)        
  
def btnclr(number):
   e1.insert(END,number)
   
def factorial():
    e1.delete(0,END)
    global fun
    fun="fact"
  
def absolute():
    e1.delete(0,END)
    global fun
    fun="abs" 
    
def pie():
    e1.insert(0,math.pi) 
    
def ln():
    e1.delete(0,END)
    global fun
    fun="ln"
    
def square():
    e1.delete(0,END)
    global fun
    fun="square"                                                                                                   
def equal():
  v=e1.get()
  e1.delete(0,END)
  if fun=="+":
    e1.insert(0,float(v) + n)
  if fun=="-":
    e1.insert(0, (float(n))-(float(v)))
  if fun=="*":
    e1.insert(0, n*float(v))
  if fun=="%":
     e1.insert(0, n%float(v))
  if fun=="/":
     e1.insert(0, n/float(v))
  if fun=="**":
     f=v[len(n)+1: ]
     e1.insert(0,float(n)**(float(f)))
  if fun=="√":
      t=float(v[1: ])
      e1.insert(0,math.sqrt(t))
  if fun=="sin":
      e1.insert(0,math.sin(float(v)))
  if fun=="cos":
      e1.insert(0,math.cos(float(v))) 
  if fun=="tan":
      e1.insert(0,math.tan(float(v)))  
  if fun== "deg":
      e1.insert(0,math.degrees(n))
      e1.insert(len(e1.get())+1,"°")   
  if fun=="sini":    
     if (-1<=float(v)<=1):
        e1.insert(0,math.asin(float(v)))
     else:
         e1.insert(0,"ERROR")   
  if fun=="cosi":  
      if (-1<=float(v)<=1):
        e1.insert(0,math.acos(float(v)))
      else:
         e1.insert(0,"ERROR")     
  if fun=="tani":  
      e1.insert(0,math.atan(float(v))) 
  if fun=="rad":  
       e1.insert(0,math.radians(float(n)))
  if fun=="log":
      e1.insert(0,math.log(float(v),10))
  if fun=="ln":
      e1.insert(0,math.log(float(v),math.e))
  if fun=="square":
      e1.insert(0,float(v)*float(v))      
  if fun=="abs":
      e1.insert(0,abs(float(v)))
  if fun=="fact":
      e1.insert(0,math.factorial(int(v)))
   
###code##
 
 
top =Tk()
top.title("welcome")
top.geometry("350x350")
frame=Frame(height="900",width="710",bg="white",)
frame.place(x=0,y=0)
lb=Label(top,text=" SCIENTIFIC CALCULATOR")
lb.place(x=65,y=10)
e1=Entry(top,bd=8,width=27)
e1.place(x=50,y=40)
 
##functions##


b6=Button(top, text="C",width=3,fg="white",bd=4,activebackground="grey",bg="green",command=clear)
b9=Button(top, text="⬅",bd=4,width=3,activebackground="white",bg="grey",fg="white",command=bksp)
b8=Button(top, text="^",bd=4,width=3,activebackground="grey",command=Exp)
b2=Button(top, text="-",bd=4,width=3,fg="white",bg="grey",command=sub)
s9=Button(top,text="log",bd=4,width=3,activebackground="grey",bg="pink",command=log)
b6.place(x=50,y=80)
b9.place(x=85,y=80)
b8.place(x=120,y=80)
b2.place(x=155,y=80)
s9.place(x=190,y=80)


n1=Button(top,text="1",bd=4,width=3,activebackground="grey",command =lambda :btnclr("1"))
n2=Button(top,text="2",bd=4,width=3,activebackground="grey",command=lambda:btnclr("2"))
n3=Button(top,text="3",bd=4,width=3,activebackground="grey",command= lambda:btnclr("3"))
b4=Button(top, text="/",bd=4,width=3,fg="white",bg="grey",command=div)
s1=Button(top,text="sin",bd=4,width=3,activebackground="black",bg="pink",command=sin)
n1.place(x=50,y=110)
n2.place(x=85,y=110)
n3.place(x=120,y=110)
b4.place(x=155,y=110)
s1.place(x=190,y=110)
 
n4=Button(top,text="4",bd=4,width=3,activebackground="grey",command=lambda:btnclr("4"))
n5=Button(top,text="5",bd=4,width=3,activebackground="grey",command=lambda:btnclr("5"))
n6=Button(top,text="6",bd=4,width=3,activebackground="grey",command=lambda:btnclr("6"))
b3=Button(top, text="x",bd=4,width=3,fg="white",bg="grey",command=mul)
s2=Button(top,text="cos",bd=4,width=3,activebackground="grey",bg="pink",command=cos)
n4.place(x=50,y=140)
n5.place(x=85,y=140)
n6.place(x=120,y=140)
b3.place(x=155,y=140)
s2.place(x=190,y=140)


n7=Button(top,text="7",bd=4,width=3,activebackground="grey",command=lambda:btnclr("7"))
n8=Button(top,text="8",bd=4,width=3,activebackground="grey",command=lambda:btnclr("8"))
n9=Button(top,text="9",bd=4,width=3,activebackground="grey",command=lambda:btnclr("9"))
b1=Button(top, text="+",bd=4,width=3,fg="white",bg="grey",command=sum)
s3=Button(top,text="tan",bd=4,width=3,activebackground="grey",bg="pink",command=tan)
n7.place(x=50,y=170)
n8.place(x=85,y=170)
n9.place(x=120,y=170)
b1.place(x=155,y=170)
s3.place(x=190,y=170)
 

 
b5=Button(top, text="%",bd=4,width=3,activebackground="grey",command=mod)
n0=Button(top,text="0",bd=4,width=3,activebackground="grey",command=lambda:btnclr("0"))
n10=Button(top,text=".",bd=4,width=3,activebackground="grey",command=lambda:btnclr("."))
s=Button(top,text="√",bd=4,width=3,fg="white",bg="grey",command=root)
s4=Button(top,text="Deg",bd=4,width=3,activebackground="grey",bg="pink",command=deg)
b5.place(x=50,y=200)
n0.place(x=85,y=200)
n10.place(x=120,y=200)
s.place(x=155,y=200)
s4.place(x=190,y=200)

 
s10=Button(top,text="ln",bd=4,width=3,fg="white",bg="grey",command=ln)
s11=Button(top,text="x²",bd=4,width=3,fg="white",bg="grey",command=square)
s12=Button(top,text="x!",bd=4,width=3,fg="white",bg="grey",command=factorial)
s13=Button(top,text="|x|",bd=4,width=3,fg="white",bg="grey",command=absolute)
s14=Button(top,text="π",bd=4,width=3,activebackground="grey",bg="pink",command=pie)
s10.place(x=50,y=230)
s11.place(x=85,y=230)
s12.place(x=120,y=230)
s13.place(x=155,y=230)
s14.place(x=190,y=230)
 
 

s5=Button(top,text="sin-",bd=4,width=3,activebackground="grey",bg="pink",command=sini)
s6=Button(top,text="cos-",bd=4,width=3,activebackground="grey",bg="pink",command=cosi)
s7=Button(top,text="tan-",bd=4,width=3,activebackground="grey",bg="pink",command=tani)
s8=Button(top,text="rad",bd=4,width=3,activebackground="grey",bg="pink",command=rad)
b7=Button(top, text="=",width=3,bd=4,fg="white",activebackground="grey",bg="green",command=equal)
s5.place(x=50,y=260)
s6.place(x=85,y=260)
s7.place(x=120,y=260)
s8.place(x=155,y=260)
b7.place(x=190,y=260)
 
top.mainloop()