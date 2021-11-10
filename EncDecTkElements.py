#!/usr/bin/env python3
from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import GROOVE
from tkinter import WORD
from tkinter import END


class MainWindow():
    """ Main Screen.
    """
    # def __init__(self, args):
    #     super(EncDecForm, self).__init__()
    #     self.args = args

    def create():
        screen = Tk()
        screen.geometry("375x398")
        screen.title("EncryptForm")
        return screen

    def encDecInputLabel(window):
        return Label(
            window,
            text="Enter text for encrypt or decript",
            fg="black",
            font=("calibri", 13)
        )

    def encDecKeyLabel(window):
        return Label(
            window,
            text="Enter key for encrypt or decrypt",
            fg="black",
            font=("calibri", 13)
        )

    def encDecInputText(window):
        return Text(
            window,
            font="Robote 20",
            bg="white",
            relief=GROOVE,
            wrap=WORD,
            bd=0
        )

    def inputKey(window):
        code = StringVar()
        return Entry(
            textvariable=code,
            width=19,
            bd=0,
            font=("arial", 25),
            show="*"
        )

    def encryptButton(window, action):
        return Button(
            text="Encrypt",
            height=2,
            width=20,
            bg="#ed3833",
            fg="white",
            bd=0,
            command=action
        )

    def decryptButton(window, action):
        return Button(
            window,
            text="Decrypt",
            height=2,
            width=20,
            bg="#00bd56",
            fg="white",
            bd=0,
            command=action
        )

    def resetButton(window, action):
        return Button(
            text="Reset",
            height=2,
            width=50,
            bg="#1089ff",
            fg="white",
            bd=0,
            command=action
        )


class EncryptWindow():
    """Encryption Window

    """
    def create(parent):
        screen = Toplevel(parent)
        screen.title("EncryptForm1")
        screen.geometry("400x200")
        screen.configure(bg="#ed3833")
        return screen

    def encryptLabel(window):
        return Label(
            window,
            text="Encrypt",
            font="arial",
            fg="white",
            bg="#ed8333"
        )

    def encryptText(window):
        return Text(
            window,
            font="Robote 10",
            bg="white",
            relief=GROOVE,
            wrap=WORD,
            bd=0
        )


class DecryptWindow():
    """Decryption Window

    """
    def createScreen(parent):
        screen = Toplevel(parent)
        screen.title("EncryptForm2")
        screen.geometry("400x200")
        screen.configure(bg="#00bd56")
        return screen

    def decryptLabel(window):
        return Label(
            window,
            text="Decrypt",
            font="arial",
            fg="white",
            bg="#00bd56"
        )

    def decryptText(window):
        return Text(
            window,
            font="Robote 10",
            bg="white",
            releif=GROOVE,
            wrap=WORD,
            bd=0
        )
