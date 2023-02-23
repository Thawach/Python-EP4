from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#--------------- csv --------------------#
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) # file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv', encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

#--------------- csv --------------------#


gui = Tk()
gui.title('โปรแกรมบันทึกข้อมูลรายการสินค้า')
gui.geometry('600x400')
L1 = Label(gui, text='โปรแกรมรายการสินค้า', font=('Angsana New',30), fg='Blue')
L1.pack()
##----------------------------##
def Button2():
    text = 'Money in account are 300 Bath' 
    messagebox.showinfo('รายการสินค้า',text)

FB1 = LabelFrame(gui, text ='สินค้า')
FB1.place(x=50,y=100)
B2 = ttk.Button(FB1, text = 'เรียกดูรายการสินค้า', command = Button2)
B2.pack(ipadx=20, ipady=20, padx = 30, pady = 20)

##----------------------------##

##-------------Section write ---------------##
LF1 = ttk.LabelFrame(gui,text = 'ใส่ข้อมูลสินค้าที่จะเพิ่มใน CSV Files')
LF1.place(x=300,y=100)

v_data = StringVar()
E1 = ttk.Entry(LF1, textvariable=v_data, font=('Angsana New', 25))
#E1.pack(padx=10,pady=10)
E1.pack()

from datetime import datetime

def saveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get()
    text = [t,data]
    writecsv(text)
    v_data.set('')

B6 = ttk.Button(LF1, text = 'บันทึกข้อมูล', command = saveData)
B6.pack(padx=10,pady=1)

##----------------------------##
gui.mainloop()
