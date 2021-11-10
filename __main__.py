#!/usr/bin/env python3
from EncDecTkElements import MainWindow
# from EncDecTkElements import EncryptWindow
# from EncDecTkElements import DecryptWindow


def encrypt():
    pass


def decrypt():
    pass


def reset():
    pass


mainWindow = MainWindow.create()

inputLabel = MainWindow.encDecInputLabel(mainWindow)
inputLabel.place(x=10, y=10)

inputText = MainWindow.encDecInputText(mainWindow)
inputText.place(x=10, y=50, width=355, height=100)

keyLabel = MainWindow.encDecKeyLabel(mainWindow)
keyLabel.place(x=10, y=170)

keyEntry = MainWindow.inputKey(mainWindow)
keyEntry.place(x=10, y=200, width=355)

encBtn = MainWindow.encryptButton(mainWindow, encrypt)
encBtn.place(x=10, y=250)

decBtn = MainWindow.decryptButton(mainWindow, decrypt)
decBtn.place(x=200, y=250)

resBtn = MainWindow.resetButton(mainWindow, reset)
resBtn.place(x=10, y=300, width=355)

mainWindow.mainloop()
