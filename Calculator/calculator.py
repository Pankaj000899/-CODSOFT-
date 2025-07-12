from tkinter import *

def clear():
    screen_entry.delete(0, END)

def Btn_Click(number):
    Entered_number = screen_entry.get()
    screen_entry.delete(0, END)
    screen_entry.insert(0, str(Entered_number) + str(number))

def ArithmeticOperation(operation):
    global first_entry,Operation
    first_entry = float(screen_entry.get())
    Operation = operation
    screen_entry.delete(0,END)

def equal():
    global first_entry,Operation
    result = 0
    second_entry=float(screen_entry.get())
    screen_entry.delete(0,END)

    if Operation=="+":
      result = first_entry + second_entry

    elif Operation=="*":
      result = first_entry * second_entry

    elif Operation=="/":
        if second_entry !=0:
            result=first_entry / second_entry
        else:
            result="Not Defined"

    elif Operation=="-":
      result = first_entry - second_entry

    screen_entry.insert(0,result)

root = Tk()

root.title("Calculator")
root.geometry("400x348")
root.maxsize(400,348)
root.minsize(400,348)

f1 = Frame(root,borderwidth = 5,relief = SUNKEN,bg = "grey")
f1.pack()

screen_entry = Entry(f1,width = 400,font = "Bierstadt 25")
screen_entry.pack()

f2 = Frame(root,borderwidth = 5, relief = SUNKEN,bg = "grey")
f2.pack()

# BUTTON
button1= Button(f2,text = "1",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(1))
button1.grid(row = 1,column = 0)

button2= Button(f2,text = "2",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(2))
button2.grid(row = 1,column = 1)

button3= Button(f2,text = "3",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(3))
button3.grid(row = 1,column = 2)

button_multiply= Button(f2,text = "X",fg = "black",bg = "yellow",width = 14, height = 4,command =  lambda: ArithmeticOperation("*"))
button_multiply.grid(row = 1,column = 3)

button4= Button(f2,text = "4",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(4))
button4.grid(row = 2,column = 0)

button5= Button(f2,text = "5",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(5))
button5.grid(row = 2,column = 1)

button6= Button(f2,text = "6",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(6))
button6.grid(row = 2,column = 2)

button_subtract= Button(f2,text = "-",fg = "black",bg = "yellow",width = 14, height = 4,command =  lambda: ArithmeticOperation("-"))
button_subtract.grid(row = 2,column = 3)

button7= Button(f2,text = "7",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(7))
button7.grid(row = 3,column = 0)

button8= Button(f2,text = "8",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(8))
button8.grid(row = 3,column = 1)

button9= Button(f2,text = "9",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(9))
button9.grid(row = 3,column = 2)

button_addition= Button(f2,text = "+",fg = "black",bg = "yellow",width = 14, height = 4,command =  lambda: ArithmeticOperation("+"))
button_addition.grid(row = 3,column = 3)

button0= Button(f2,text = "0",fg = "black",bg = "orange",width = 12, height = 4,command =  lambda: Btn_Click(0))
button0.grid(row = 4,column = 0)

button_clear= Button(f2,text = "C",fg = "black",bg = "green",width = 12, height = 4,command = clear)
button_clear.grid(row = 4,column = 1)

button_equal= Button(f2,text = "=",width = 12, height = 4,fg = "black",bg = "green",command = equal)
button_equal.grid(row = 4,column = 2)

button_division= Button(f2,text = "/",fg = "black",bg = "yellow",width = 14, height = 4,command =  lambda: ArithmeticOperation("/"))
button_division.grid(row = 4,column = 3)

root.mainloop()
