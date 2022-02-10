from tkinter import *
from tkinter import messagebox
import random as r

#FOR BOTTON
def button(frame):
    b=Button(frame,padx=1,bg="#000000",width=3,text="    ", font=("arial",60,"bold"),relief=RAISED,bd=5)
    return b

#FOR APPLY CHANGE ON BUTTON
def change():
    global a
    for i in ["O","X"]:
        if not (i == a):
            a = i
            break

#FOR RESET GAME
def reset():
    global a
    for i in range(3):
        for j in range(3):
            b[i][j]["text"] = " "
            b[i][j]["state"] = NORMAL
    a=r.choice(["O","X"])

#FOR CHECK WINNER
def check():
    for i in range(3):
        if (b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
            messagebox.showinfo("Congrats !!! ", "'"+a+"'has Won")
            reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats !!!","'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showwarning("Tied !!!","The match ended in a draw")
        reset()

#APPLY CLICK ANIMATION
def click(row,col):
    b[row][col].config(text=a,state=DISABLED, disabledforeground=colour[a])
    check()
    change()

# -------------------------------------------::::::::::::: MAIN :::::::::::::--------------------------------------

root = Tk()
root.title("---------------------------::::::Tic Tac Toe::::::---------------------------- ")
a = r.choice(["O","X"])
colour ={"O":"deep sky blue", "X":"yellow"}
b = [[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
reset_btn = Button(text="Reset Game",font=('arial',15,'bold'),command=reset)
reset_btn.grid(row=3,column=0,columnspan=3)
root.mainloop()
