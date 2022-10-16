
import tkinter as tk
global xo,no
X="X"
O="O"
b1=b2=b3=b4=b5=b6=b7=b8=b9=tk.Button()
theBoard = {
            1 : '  ' , 2 : '  ',3 : '  ',
            4 : '  ' , 5 : '  ',6 : '  ',
            7 : '  ' , 8 : '  ',9 : '  ' 
          }

def win(b,a):
    if theBoard[7]==theBoard[8]==theBoard[9] == b or theBoard[4]==theBoard[5]==theBoard[6] ==b or theBoard[1]==theBoard[2]==theBoard[3] ==b or theBoard[1]==theBoard[4]==theBoard[7] == b or theBoard[2]==theBoard[5]==theBoard[8] ==b or theBoard[3]==theBoard[6]==theBoard[9] ==b or theBoard[7]==theBoard[5]==theBoard[3] ==b or theBoard[1]==theBoard[5]==theBoard[9] ==b :
        winlab = tk.Label(root,text="The Player X won ",bg=Bg,fg=Fg,font=80,).grid(row=4,column=0,columnspan=3)
    else :
        winlab=tk.Label(root, text="The player O won ",bg=Bg,fg=Fg,font=80)
     

num=0
xo="X"
def on_click7():
    global xo,num
    theBoard[7]=xo
    x= tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click7).grid(row= 1, column=0)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)

def on_click8():
    global xo,num
    theBoard[8]=xo
    x= tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click8).grid(row= 1, column=1)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)

def on_click9():
    global xo,num
    theBoard[9]=xo 
    x= tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click9).grid(row= 1, column=2)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)

def on_click4():
    global xo,num
    theBoard[4]=xo
    x=tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click4).grid(row= 2, column=0)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)

def on_click5():
    global xo,num
    theBoard[5]=xo
    x= tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click5).grid(row= 2, column=1)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)

def on_click6():
    global xo,num
    theBoard[6]=xo
    x= tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click5).grid(row= 2, column=2)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)

def on_click1():
    global xo,num
    theBoard[1]=xo
    x=tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click1).grid(row= 3, column=0)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)

def on_click2():
    global xo,num
    theBoard[2]=xo
    x= tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click2).grid(row= 3, column=1)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)

def on_click3():
    global xo,num
    theBoard[3]=xo
    x= tk.Button(root,bg=Bg,fg=Fg,text=xo,padx=xy,pady=xy,command=on_click3).grid(row= 3, column=2)
    if xo=='X' :
         xo="O" 
         num+=1
    else : 
        xo="X"
        num+=1 
    if num>3:
        win(X,O)


root =tk.Tk()
root.title('Tic Tac Toe')
Bg="black" 
Fg="White"
font= 52
xy=50
title =tk.Label(root,text="Tic Tac Toe",bg=Bg,fg=Fg,font=30,padx=50,pady=20).grid(rowspan=1,row=0,column=0,columnspan=3)

b7= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click7).grid(row= 1, column=0)
b8= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click8).grid(row= 1, column=1)
b9= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click9).grid(row= 1, column=2)

b4= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click4).grid(row= 2, column=0)
b5= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click5).grid(row= 2, column=1)
b6= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click6).grid(row= 2, column=2)

b1= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click1).grid(row= 3, column=0)
b2= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click2).grid(row= 3, column=1)
b3= tk.Button(root,bg=Bg,fg=Fg,padx=xy,pady=xy,command=on_click3).grid(row= 3, column=2)

root.configure(bg="black")
root.mainloop()
