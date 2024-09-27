# import all the classes, functions and variables from the tkinter package
from tkinter import *
import tkinter as tk
#button function
def button_clicked():
    print("Registered")
#creating the graphical window using tk()
root = tk.Tk()
#creating a label widget
Label(root, text = 'Registration Form').grid(row=0)
#name 
Label(root, text = 'User Name').grid(row=1)
n=Entry(root)
n.grid(row=1, column=1)
#password
Label(root, text = 'Password').grid(row=2)
p=Entry(root)
p.grid(row=2, column=1)
#email
Label(root, text = 'E-mail').grid(row=3)
e=Entry(root)
e.grid(row=3, column=1)
#Activity intrested
Label(root, text = 'Activity intrested').grid(row=4)
r=IntVar()
Radiobutton(root, text='Web-Programming', variable=r,value=1).grid(row=5)
Radiobutton(root, text='Data Analytics', variable=r,value=2).grid(row=5,column=1)
Radiobutton(root, text='AI|ML', variable=r,value=3).grid(row=5,column=2)
#submit button
button = tk.Button(root,text="Submit", command=button_clicked,activebackground="Green",activeforeground="white",bg="lightgray",disabledforeground="gray",fg="black").grid(row=7,column=1)
#The application window does not appear before you enter the main loop
root.mainloop()
