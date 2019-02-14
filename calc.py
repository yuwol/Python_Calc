## Simple calculator by Michael. ##
## 13.02.2019 v0.1 Accept multiple calculation. ex) 1 * 2 / (1+2) - (4 * 7) = -27.333333333333332
## 14.02.2019 v0.2 Accept keyboard input. 0~9 and {-+*/}, esc (clear). =, enter (get result)
            
from tkinter import *
import tkinter.messagebox as mb

Root = Tk()
Root.title("Michael's Calculator")
Root.configure(background="#cceeff")
Root.geometry("600x900") #GUI size
Root.resizable(0,0) 

def key_input(value):
    # 쉬프트키 입력 무시.(덧셈할때)
    if not repr(value.char) == "''":    	
        accepted = '1234567890/*+-.=()'

        if (value.char in accepted) :
        	calc(value.char)
        elif value.keysym == "Return" :            
            calc('=')
        elif value.keysym == "Escape":
            calc('C')
        elif value.keysym == "BackSpace":
            calc('<-')
        else :
        	print(value.char)

def calc(Oper):
	try:
		if Oper == 'C': 
			ent.delete(0, END) 
		elif Oper =='AC':
			ent.delete(0, END)
			ent0.delete(1.0, END)
		elif Oper == '<-':
			ent.delete(len(ent.get())-1, END)
		elif Oper == '=': 
			ans = eval(ent.get())
			history =ent.get()
			history2 =str(ans)
			history3 =str(history+" = ")+str(history2+" "+'\n') # make it str for line break
			ent.delete(0, END) 
			ent.insert(0, ans) 
			ent0.insert(0.0,history3)
		else:
			ent.insert(END,Oper) 
	except:
		msg="Please check your equation."
		mb.showinfo("Information",msg)
		display.delete(0,END)

calcLabel = Label(Root, text="equation", width=20, bg='#cceeff', font=("verdana", "12","bold"))
calcLabel.pack(anchor=N, padx=10, pady=10)
calcLabel.place(width=150, height=30, x=30, y=10)

historyLabel = Label(Root, text="calc history", width=20, bg='#cceeff', font=("verdana", "12","bold"))
historyLabel.pack(anchor=N, padx=10, pady=10)
historyLabel.place(width=150, height=30, x=260, y=10)

ent0 = Text(Root) 
ent0.pack()
ent0.place(width=195, height=60, x=240, y=45)

ent = Entry(Root)
ent.insert(0, ' ')
ent.pack()
ent.place(width=195, height=60, x=10, y=45) # set ent size, location

Clearbt = Button(Root, text='AC', fg='#FA5858', bg='#A9F5D0', font=("verdana", "25","bold"), command=(lambda Oper='AC':calc(Oper)))
Clearbt.pack()
Clearbt.place(width=75,height=150,x=450,y=0) # set button size, location

Clearbt = Button(Root, text='C', fg='#FA5858', bg='#A9F5D0', font=("verdana", "25","bold"), command=(lambda Oper='C':calc(Oper)))
Clearbt.pack()
Clearbt.place(width=75, height=150, x=525, y=0)

Clearbt = Button(Root, text='<-', bg='#EFFBF2', font=("verdana", "13"), command=(lambda Oper='<-':calc(Oper)))
Clearbt.pack()
Clearbt.place(width=150, height=150, x=450, y=150)

buttons = ['()%','123/', '456*', '789+', '.0-=']
xp=0
yp=150
for i in buttons: # draw buttons
	for j in i:
		if (xp == 450) or (yp == 150):
			bt = Button(Root, text=j, bg='#EFFBF2', font=("verdana", "13"), command=(lambda Oper=j:calc(Oper)))
		else:		
			bt = Button(Root, text=j, bg='#ffffff', font=("verdana", "13"), command=(lambda Oper=j:calc(Oper)))
		bt.pack()
		bt.place(width=150, height=150, x=xp, y=yp)
		xp+=150
	yp+=150
	xp=0 

Root.bind('<Key>',key_input)
Root.mainloop()
