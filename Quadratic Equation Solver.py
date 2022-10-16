
import math
import tkinter as tk

root =tk.Tk()
myStringA =tk.StringVar(root)
myStringC =tk.StringVar(root)
myStringB=tk.StringVar(root)

def on_click():
    a= float(myStringA.get()) 
    b= float(myStringB.get())
    c=float( myStringC.get()) 
    dis =math.pow(b,2)-4*a*c
    print(str(dis)+"\t the discreamenabt\n\n\n\n\n\n\n\n\n\n\n\n")
    if dis>0:
        d1 = (-b + math.sqrt(dis)) / 2*a
        d2 = (-b - math.sqrt(dis)) / 2*a
        label =tk.Label(root,text="Roots of the equation =\t"+str(d1)+"\tand\t"+str(d2),fg="white",bg="Black",height=4,font=30)
        label.grid(row=5,column=0)
    else :
        label =tk.Label(root,text="Not a Quadratic Equation ",fg="white",bg="Black",height=4,font=30)
        label.grid(row=5,column=0)


t ="Enter the values of a b and c of the ax² + bx + c = 0 \n\trespectively in the boxes given below"
lab = tk.Label(root,text='Quadratic Equations Solver',bg='Black',fg='White',justify='center',font=41).grid(row=0,column=0)
lab2 =tk.Label(root, text=t,fg='white',bg="black" ,justify='center',font=41).grid(row=1,column=0)

alab =tk.Label(root, text='Enter for a ',fg='white',bg='Black',font=40).grid(row=2,column=0)
var_1=tk.Entry(root,textvariable=myStringA,fg="white", background="black",font=40).grid(row=2,column=1)

blab =tk.Label(root, text='Enter for b ',fg='white',bg='Black',font=40).grid(row=3,column=0)
var_2=tk.Entry(root,textvariable=myStringB,fg="white", background="black",font=20).grid(row=3,column=1)

clab =tk. Label(root, text='Enter for c ',fg='white',bg='Black',font=40).grid(row=4,column=0)
var_3=tk.Entry(root,textvariable=myStringC,fg="white", background="black",font=20).grid(row=4,column=1)



submit = tk.Button(root,text="Submit",fg='white',bg='black',font=20,command=on_click).grid(row=5,column=1)
root.title('Quadratic Equation Solver')
root.configure(bg='black')
root.mainloop()




    




