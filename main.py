from tkinter import END

import interface
import generator

def generate():
    interface.plaintextbox.delete(0, END)
    lowercase=interface.lowercase.get()
    numbers=interface.numbers.get()
    uppercase=interface.uppercase.get()
    symbel=interface.symbel.get()

    a=int(interface.spin_lowercase.get())
    s=int(interface.spin_numbers.get())
    d=int(interface.spin_uppercase.get())
    f=int(interface.spin_symbel.get())

    for i in range(5):
        v=generator.generate_password(lowercase,numbers,uppercase,symbel,a,s,d,f)
        interface.plaintextbox.insert(END, v)

interface.button.config(command=generate)

interface.window.mainloop()