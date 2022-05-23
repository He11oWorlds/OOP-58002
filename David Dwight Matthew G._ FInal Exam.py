from tkinter import *
exam = Tk()

exam.geometry("360x200")
exam.title ("Final Exam")

def minimum():
    L = []
    num1 = eval(input("Enter the first number:"))
    L.append(num1)
    num2 = eval(input("Enter the second number:"))
    L.append(num2)
    num3 = eval(input("Enter the third number:"))
    L.append(num3)
    print("The smallest number among the three is:", str(min(L)))

label1 = Label(exam, text = "Finding the Smallest Number")
label1.grid(row=0, column=1, columnspan=2,sticky=EW)

label2 = Label(exam,text = "Enter the first number:")
label2.grid(row=1, column = 0,sticky=W)
sinigang = StringVar()
entry2 = Entry(exam,bd=3,textvariable=computer)
entry2.grid(row=1, column = 1)

label3 = Label(exam,text = "Enter the second number:")
label3.grid(row=2, column=0)
adobo = StringVar()
entry3 = Entry(exam,bd=3,textvariable=phone)
entry3.grid(row=2,column=1)

label4 = Label(exam,text="Enter the third number:")
label4.grid(row=3,column =0, sticky=W)
paksiw = StringVar()
entry4 = Entry(exam,bd=3,textvariable=laptop)
entry4.grid(row=3, column=1)

button1 = Button(exam,text = "Find the smallest number",command=minimum)
button1.grid(row=4, column = 1)

label5 = Label(exam,text="The least number:")
label5.grid(row=5,column=0,sticky=W)
tinola = StringVar()
entry5 = Entry(exam,bd=3,state="readonly",textvariable=watch)
entry5.grid(row=5,column=1)

mainloop()