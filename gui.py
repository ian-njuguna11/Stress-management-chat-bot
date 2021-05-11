from tkinter import *
import tkinter as tk

r = tk.Tk()

def send():
    send = "You => "+ e.get()
    txt.insert(END,"\n"+send)
    if e.get() == "hello":
        txt.insert(END, "\n" + "Counsellor => Hello")
    e.delete(0,END)

txt = Text(r,bg = "green")
txt.grid(row=0,column=0,columnspan=2)
e=Entry(r, width='100',bg = 'blue')
send=Button(r,text="Send",command=send,bg = "green").grid(row=1,column=1)
e.grid(row=1,column=0)
r.title('Counsellor Chatbot ')
r.mainloop()

