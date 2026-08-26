from krita import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import random as r 
import pyperclip as clip

hexes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
inst = Krita.instance()
print(inst)

newDoc = inst.createDocument(50, 50, "untitled", "RGBA", "U8", "", 67.0)

inst.activeWindow().addView(newDoc)

myaction = QAction("gambling")

def func():
    print("maybe i do know how to code", flush=True)
    x = 0
    hexcode = "#"
    while x <= 5:
        value = r.randint(0, 14)
        strhex = hexes[value]
        hexcode += strhex
        x += 1
    clip.copy(hexcode)
    clip.paste()
    mybutton.setText(hexcode + "(click to copy color and get a new one!)")
myaction.triggered.connect(func)

mypopup = QDialog()
mypopup.setWindowTitle("my awesome popup")

mylayout = QVBoxLayout()
mybutton = QPushButton("click me!")

mybutton.clicked.connect(func)

mylayout.addWidget(mybutton)
mypopup.setLayout(mylayout)

mainmenu = Krita.instance().activeWindow().qwindow().menuBar()
mymenu = mainmenu.addMenu("my menu")

def openpopup():
    mypopup.exec()

mymenuitem = QAction("run action")
mymenuitem.triggered.connect(openpopup)

mymenu.addAction(mymenuitem)