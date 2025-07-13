from tkinter import *
import tkinter.messagebox as tm
import random
import string

def Pass_Generator():
    l =length_entry.get()
    try:
        l = int(l)
    except:
        tm.showwarning("Error", "Please Enter a Valid Length")

    password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k=l))

    Password_listbox.delete(0, END)
    Password_listbox.insert(0, password)

root = Tk()

root.geometry("400x400")
root.resizable(False,False)
root.title("Password generator by Pankaj")
root.configure(bg = "grey")
Label(root,text="Password Generator",font = "Bierstadt 20 bold",bg = "grey",fg ="white").pack()

frame = Frame(root)
frame.pack(pady = 10)

Label(frame, text = "Enter The Length",font = "Bierstadt 15",fg = "blue").grid(row = 0, column = 0)

length_entry = Entry(frame,font = "Bierstadt 15")
length_entry.grid(row = 0, column = 1)

Button(root,text = "Generate password",font = "Bierstadt 15",fg = "white",bg = "black",command = Pass_Generator).pack()

f2 = Frame(root)
f2.pack(pady = 10)

Password_listbox = Listbox(f2,font = "Bierstadt 20",height =1,width = 50)
Password_listbox.pack(pady = 10)

root.mainloop()
