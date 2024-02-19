# -*- coding: utf-8 -*-
from tkinter import *

window = Tk()
window.geometry('400x500')
window.title('Canvas')

lowercase=BooleanVar()
uppercase=BooleanVar()
numbers=BooleanVar()
symbel=BooleanVar()

loc=LabelFrame()

check_lowercase=Checkbutton(loc,text='abcdefghijklmnopqrstuvwxyz',variable=lowercase,offvalue=False,onvalue=True)
check_uppercase=Checkbutton(loc,text='ABCDEFGHIJKLMNOPQRSTUVWXYZ',variable=uppercase,offvalue=False,onvalue=True)
check_numbers=Checkbutton(loc,text='1234567890',variable=numbers,offvalue=False,onvalue=True)
check_symbel=Checkbutton(loc,text='!@#$%^&*()',variable=symbel,offvalue=False,onvalue=True)
plaintextbox=Listbox(loc)
button=Button(loc,text='Сгенерировать пароль')

spin_lowercase=Spinbox(loc,width=3,from_=1,to_=8)
spin_uppercase=Spinbox(loc,width=3,from_=1,to_=8)
spin_numbers=Spinbox(loc,width=3,from_=1,to_=8)
spin_symbel=Spinbox(loc,width=3,from_=1,to_=8)



loc.pack(fill=X)
check_lowercase.grid(sticky=W,padx=10,pady=10)
check_uppercase.grid(sticky=W,padx=10,pady=10)
check_numbers.grid(sticky=W,padx=10,pady=10)
check_symbel.grid(sticky=W,padx=10,pady=10)

spin_lowercase.grid(column=1,row=0)
spin_uppercase.grid(column=1,row=1)
spin_numbers.grid(column=1,row=2)
spin_symbel.grid(column=1,row=3)

plaintextbox.grid(columnspan=3)
button.grid(padx=10,pady=10,columnspan=3)

if __name__=='__main__':
    window.mainloop()