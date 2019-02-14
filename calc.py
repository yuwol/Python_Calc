from tkinter import *
import tkinter.messagebox as mb

Root=Tk()
Root.title("빠딱")
Root.configure(background="#cceeff") #기본 바탕색 지정
Root.geometry("600x900") # 창이 뜰 때 기본적인 크기 지정
Root.resizable(0,0) #창의 크기를 조절 못하게 함

#calc
def calc(Oper):
	try:
		if Oper == 'C': #C라는 인자가 들어오면 실행되는 함수
			ent.delete(0, END) #ent의 처음부터 끝까지 삭제하여라
		elif Oper =='AC':
			ent.delete(0, END)
			ent0.delete(1.0, END)
		elif Oper == '<-':
			ent.delete(len(ent.get())-1, END) #ent의 길이를 구해서 딜리트 구현
		elif Oper == '=': #eval함수는 문자열로된 값을 모두 calc해주는 내장 함수
			ans = eval(ent.get())
			history =ent.get()
			history2 =str(ans)
			history3 =str(history+" ")+str(history2+" "+'\n')#줄띄우기를 하려고 문자열화
			ent.delete(0, END) #먼저 입력값을 지우고
			ent.insert(0, ans) #답을 출력
			ent0.insert(0.0,history3)#history
		else:
			ent.insert(END,Oper) #끝에서부터 입력되는 값을 계속 넣어주는 역할
	except:
		msg="calc방식이 잘못되었습니다."
		mb.showinfo("Information",msg)
		display.delete(0,END)

calclabel = Label(Root, text="calc", width=10,bg='#cceeff',font =("verdana", "12","bold")) #label로 꾸미기
calclabel.pack(anchor=N, padx=10, pady=10)
calclabel.place(width=40,height=30,x=87 ,y=10)

historylabel = Label(Root, text="history", width=10,bg='#cceeff',font =("verdana", "12","bold"))
historylabel.pack(anchor=N, padx=10, pady=10)
historylabel.place(width=40,height=30,x=317,y=10)

ent0=Text(Root) #Entry는 한줄 텍스트칸이라 줄바꾸기 x
ent0.pack()
ent0.place(width=195,height=60,x=240,y=45)

ent=Entry(Root)
ent.insert(0, ' ')
ent.pack()
ent.place(width=195,height=60,x=10,y=45)#엔트리 크기,위치 지정



Clearbt = Button(Root,text='AC',fg='#FA5858',bg='#A9F5D0',font = ("verdana", "25","bold"),command=(lambda Oper='AC':calc(Oper)))
#AC를 누르면 위의 함수로 가서 맞는 함수를 적용
Clearbt.pack()
Clearbt.place(width=75,height=150,x=450,y=0)#버튼 크기,위치 지정

Clearbt = Button(Root,text='C',fg='#FA5858',bg='#A9F5D0',font = ("verdana", "25","bold"),command=(lambda Oper='C':calc(Oper)))
Clearbt.pack()
Clearbt.place(width=75,height=150,x=525,y=0)

Clearbt = Button(Root,text='<-',bg='#EFFBF2',font = ("verdana", "13"),command=(lambda Oper='<-':calc(Oper)))
Clearbt.pack()
Clearbt.place(width=150,height=150,x=450,y=150)

buttons = ['()%','123/', '456*', '789+', '.0-=']
xp=0
yp=150
for i in buttons:
	for j in i:
		bt = Button(Root,text=j,bg='#EFFBF2',font = ("verdana", "13"),command=(lambda Oper=j:calc(Oper)))
		bt.pack()
		bt.place(width=150,height=150,x=xp,y=yp)
		xp+=150
	yp+=150
	xp=0 #xp를 buttons의 ,마다 초기화

Root.mainloop()
