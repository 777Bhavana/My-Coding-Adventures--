
from tkinter import *
import tkinter


root = Tk()
root.title('Boyle\'s Law')
myStringA =tkinter.StringVar(root)
myStringC =tkinter.StringVar(root)
myStringB=tkinter.StringVar(root)



def p1_constant(v1,p2,v2):
    p1 =p2*v2/v1
    return p1

def v1_constant(p1,p2,v2):
    v1=p2*v2/p1
    return v1

def p2_constant(p1,v1,v2):
    p2=p1*v1/v2
    return p2

def v2_constant(p1,v1,p2):
    v2=p1*v1/p2
    return v2



def click_p1():
    def doit_p1():
            v1= float(myStringA.get())
            p2= float(myStringB.get())
            v2=float( myStringC.get())
            p1=p1_constant(v1,p2,v2)
            answer =tkinter.Label(root,text='The value of P1 is =\t'+str(p1),fg='white',bg='black',font=80).grid(row=6,column=1,columnspan=6) 
            

    lab = tkinter.Label(root,bg='black',fg='white',text='Enter v1 p2 v2 in the boxes below ',font=80).grid(row=4,column=0,columnspan=6)
    E_v1 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringA,font=40).grid(row=5,column=0)
    E_p2 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringB,font=40).grid(row=5,column=1)
    E_v2 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringC,font=40).grid(row=5,column=2)
    submit =tkinter.Button(root,bg='black',fg='white',text='SUBMIT',font=40,command=doit_p1).grid(row=5,column=3)

    
    

def click_v1() :
    def doit_v1():
            p1= float(myStringA.get())
            p2= float(myStringB.get())
            v2=float( myStringC.get())
            v1=v1_constant(p1,p2,v2)
            answer =tkinter.Label(root,text='The value of V1 is =\t'+str(v1),fg='white',bg='black',font=80).grid(row=6,column=1,columnspan=6) 
            

    lab = tkinter.Label(root,bg='black',fg='white',text='Enter p1 p2 v2 in the boxes below ',font=80).grid(row=4,column=0,columnspan=6)
    E_p1 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringA,font=40).grid(row=5,column=0)
    E_p2 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringB,font=40).grid(row=5,column=1)
    E_v2 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringC,font=40).grid(row=5,column=2)
    submit =tkinter.Button(root,bg='black',fg='white',text='SUBMIT',font=40,command=doit_v1).grid(row=5,column=3)  

def click_v2():
    def doit_v2():
            p1= float(myStringA.get())
            v1= float(myStringB.get())
            p2=float( myStringC.get())
            v2=v2_constant(p1,v1,p2)
            answer =tkinter.Label(root,text='The value of V2 is =\t'+str(v2),fg='white',bg='black',font=80).grid(row=6,column=1,columnspan=6) 
            

    lab = tkinter.Label(root,bg='black',fg='white',text='Enter p1 v1 v2 in the boxes below ',font=80).grid(row=4,column=0,columnspan=6)
    E_p1 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringA,font=40).grid(row=5,column=0)
    E_p2 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringB,font=40).grid(row=5,column=1)
    E_v2 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringC,font=40).grid(row=5,column=2)
    submit =tkinter.Button(root,bg='black',fg='white',text='SUBMIT',font=40,command=doit_v2).grid(row=5,column=3)

def click_p2():
    def doit_p2():
            p1= float(myStringA.get())
            v1= float(myStringB.get())
            v2=float( myStringC.get())
            p2=p1_constant(p1,v1,v2)
            answer =tkinter.Label(root,text='The value of P2 is =\t'+str(p2),fg='white',bg='black',font=80).grid(row=6,column=1,columnspan=6) 
            

    lab = tkinter.Label(root,bg='black',fg='white',text='Enter p1 v1 v2 in the boxes below ',font=80).grid(row=4,column=0,columnspan=6)
    E_p1 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringA,font=40).grid(row=5,column=0)
    E_p2 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringB,font=40).grid(row=5,column=1)
    E_v2 =tkinter.Entry(root,bg='black',fg='white',textvariable=myStringC,font=40).grid(row=5,column=2)
    submit =tkinter.Button(root,bg='black',fg='white',text='SUBMIT',font=40,command=doit_p2).grid(row=5,column=3) 




op  =tkinter.Label(root,text='\tBOYLE\'S LAW CALCULATOR\t',bg='black',fg='white',font=100,justify='center').grid(row=0,column=0,columnspan=6)
op2 =tkinter.Label(root,text='\tENTER p1 v1 p2 or v2 AS CONSTANT TO FIND\t',bg='black',fg='white',font=95,justify='center').grid(row=1,column=0,columnspan=6)

_v1 =tkinter.Button(root,text='\tV1\t',command=click_v1,fg='white',bg='black',font=80).grid(row=2,column=0)
_p1 =tkinter.Button(root,text='\tP1\t',command=click_p1,fg='white',bg='black',font=80).grid(row=2,column=1)
_p2 =tkinter.Button(root,text='\tV2\t',command=click_v2,fg='white',bg='black',font=80).grid(row=2,column=2)
_v2 =tkinter.Button(root,text='\tP2\t',command=click_p2,fg='white',bg='black',font=80).grid(row=2,column=3)





root.configure(bg='black')
root.mainloop()