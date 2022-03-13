# Elden Ring - Simple Trainer

**Executable trainer maded on python.**

**Instructions**
>Open Elden Ering

>Open Trainer with administrator!!!

>Mark what checkboxes you want.

*SourceCode:*

```
#Write and Read Memory imports
from pymem import *
from pymem.process import *

#GUI imports
from doctest import master
from tkinter import *
import tkinter

#Hack
pm = Pymem("eldenring.exe")

gameModule = module_from_name(pm.process_handle, "eldenring.exe").lpBaseOfDll

#Hack Base
def GetPtrAddr (base, offsets):
    addr = pm.read_longlong(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_longlong(addr + i)
    return addr + offsets[-1]

#Hack functions
def Runes():
    pm.write_int(GetPtrAddr(gameModule + 0x04475968, [0x318, 0xB0, 0x230, 0x340, 0x7C8, 0x7C]), 900000000)
    master.after(1000, Runes)

def CrimsonTears():
    pm.write_int(GetPtrAddr(gameModule + 0x03C4B238, [0x5B8, 0x58, 0x20, 0xF8, 0x248, 0x198, 0x134]), 40)
    master.after(1000, CrimsonTears)

def Health():
    pm.write_int(GetPtrAddr(gameModule + 0x044757B8, [0x38, 0x30, 0x298, 0x10, 0x8, 0x10, 0x5C8]), 4000)
    master.after(1000, Health)

#GUI (structure)
master = tkinter.Tk(className='ishidaw trainer')
master.geometry("280x220")
master.resizable(False, False)

master.configure(bg='#3b3b3b')

Label(master, text="Elden Ring Trainer - 1.00",font=("Arial bold", 16), anchor="center").pack(pady=20)


#Part of GUI (varibles, checkmarks and mainloop)
CheckValueRunes = tkinter.BooleanVar()
CheckValueCrimson = tkinter.BooleanVar()
CheckValueHealthPoints = tkinter.BooleanVar()

FirstCheck = tkinter.Checkbutton(master, text='Infinite Runes', command=Runes,var=CheckValueRunes).pack()
SecondCheck = tkinter.Checkbutton(master, text='Crimsom Tears', command=CrimsonTears, var=CheckValueCrimson).pack(pady=10)
ThirdCheck = tkinter.Checkbutton(master, text='Infinite HP', command=Health, var=CheckValueHealthPoints).pack()

master.mainloop()

#Author: Ishidaw \[T]/
```
To make an executable I used pyinstaller, all in one.

```
pip install pyinstaller
```
