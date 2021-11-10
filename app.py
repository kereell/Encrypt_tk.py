#!/usr/bin/env python3
from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import GROOVE
from tkinter import WORD
from tkinter import END
from tkinter import Toplevel
from tkinter import messagebox
import base64


def decrypt():
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(screen0)
        screen2.title("EncryptForm2")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text0.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        label3 = Label(
            screen2,
            text="Decrypt",
            font="arial",
            fg="white",
            bg="#00bd56"
        )
        label3.place(x=10, y=0)

        text3 = Text(
            screen2,
            font="Robote 10",
            bg="white",
            relief=GROOVE,
            wrap=WORD,
            bd=0
        )
        text3.place(x=10, y=40, width=380, height=150)
        text3.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("EncryptForm2", "Input Password")
    elif password != "1234":
        messagebox.showerror("EncryptForm2", "Invalid Password")


def encrypt():
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(screen0)
        screen1.title("EncryptForm1")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text0.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        label2 = Label(
            screen1,
            text="Encrypt",
            font="arial",
            fg="white",
            bg="#ed3833"
        )
        label2.place(x=10, y=0)

        text2 = Text(
            screen1,
            font="Robote 10",
            bg="white",
            relief=GROOVE,
            wrap=WORD,
            bd=0
        )
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("EncryptForm1", "Input Password")
    elif password != "1234":
        messagebox.showerror("EncryptForm1", "Invalid Password")


def main_screen():
    global screen0
    global code
    global text0

    screen0 = Tk()
    screen0.geometry("375x398")
    # icon
    # Fuck the icon
    screen0.title("EncryptForm")

    label0 = Label(
        text="Enter text for encryption & decription",
        fg="black",
        font=("calibri", 13)
    )

    label1 = Label(
        text="Enter key for encryption & decription",
        fg="black",
        font=("calibri", 13)
    )

    text0 = Text(
        font="Robote 20",
        bg="white",
        relief=GROOVE,
        wrap=WORD,
        bd=0,
    )

    code = StringVar()
    entry0 = Entry(
        textvariable=code,
        width=19,
        bd=0,
        font=("arial", 25),
        show="*"
    )

    def reset():
        code.set("")
        text0.delete(1.0, END)

    button0 = Button(
        text="Encrypt",
        height=2,
        width=20,
        bg="#ed3833",
        fg="white",
        bd=0,
        command=encrypt
    )

    button1 = Button(
        text="Decrypt",
        height=2,
        width=20,
        bg="#00bd56",
        fg="white",
        bd=0,
        command=decrypt
    )

    button2 = Button(
        text="Reset",
        height=2,
        width=50,
        bg="#1089ff",
        fg="white",
        bd=0,
        command=reset
    )

    label0.place(x=10, y=10)
    text0.place(x=10, y=50, width=340, height=100)
    label1.place(x=10, y=170)
    entry0.place(x=10, y=200, width=340)
    button0.place(x=10, y=250)
    button1.place(x=200, y=250)
    button2.place(x=10, y=300)

    screen0.mainloop()


main_screen()
