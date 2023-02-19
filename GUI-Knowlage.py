from tkinter import*
from tkinter import ttk
from tkinter import messagebox

GUI=Tk()
GUI.title('บันทึกรายรับ-รายจ่ายประจำวัน')
GUI.geometry('500x400')
canvas = Canvas(GUI,width=500,height=400)
photo = PhotoImage(file='bnk.png')
canvas.create_image(0,0,image=photo,anchor=NW)
canvas.place(x=0,y=0)

L1=Label(GUI,text='บันทึกรายรับ-รายจ่าย',font=('Angsana New',28),fg='blue')
L1.place(x=150,y=30)

#############date
def Button1():
    text='14/02/23'
    messagebox.showinfo('ระบุวัน',text)

FB1=Frame(GUI)
FB1.place(x=20,y=80)
B1=ttk.Button(FB1,text='วัน/เดือน/ปี',command=Button1)
B1.pack(ipadx=10,ipady=10)

#############
L2=Label(GUI,text='----รายการ----',font=('Angsana New',14,'bold'),fg='green')
L2.place(x=20,y=130)
############
def Button2():
    text='เงินเดือน 1500 บาท'
    messagebox.showinfo('รายการ',text)

FB2=Frame(GUI)
FB2.place(x=45,y=180)
B2=ttk.Button(FB2,text='รายรับ',command=Button2)
B2.pack(ipadx=10,ipady=10)
###########
def Button3():
    text='กินข้าว 30 บาท'
    messagebox.showinfo('รายการ',text)

FB3=Frame(GUI)
FB3.place(x=45,y=240)
B3=ttk.Button(FB3,text='รายจ่าย',command=Button3)
B3.pack(ipadx=10,ipady=10)

GUI.mainloop()
