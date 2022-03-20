#Write and Read Memory imports
from pymem import *
from pymem.process import *

#GUI imports
import tkinter as tk

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
    app.after(1000, Runes)

def CrimsonTears():
    pm.write_int(GetPtrAddr(gameModule + 0x03C4B238, [0x5B8, 0x58, 0x20, 0xF8, 0x248, 0x198, 0x134]), 40)
    app.after(1000, CrimsonTears)

def Health():
    pm.write_int(GetPtrAddr(gameModule + 0x044757B8, [0x38, 0x30, 0x298, 0x10, 0x8, 0x10, 0x5C8]), 4000)
    app.after(1000, Health)

#GUI
app = tk.Tk()

app.title('ER - Trainer')
app.geometry("280x220")
app.resizable(False, False)

#grid settings
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)

#Transform checkboxes in True or False (boolean values)
CheckValueRunes = tk.BooleanVar()
CheckValueCrimson = tk.BooleanVar()
CheckValueHealthPoints = tk.BooleanVar()

#Checkboxes
FirstCheck = tk.Checkbutton(app, text="Infinite Runes  ", command=Runes,var=CheckValueRunes)
SecondCheck = tk.Checkbutton(app, text="Infinite Crimson", command=CrimsonTears, var=CheckValueCrimson)
ThirdCheck = tk.Checkbutton(app, text="Infinite Health ", command=Health, var=CheckValueHealthPoints)

#Title
TitleLabel = tk.Label(app ,text="Elden Ring Trainer")
TitleLabel.configure(font=("Cascadia Code", 18))

#Font config from checkboxes
FirstCheck.configure(font=("Cascadia Code", 10))
SecondCheck.configure(font=("Cascadia Code", 10))
ThirdCheck.configure(font=("Cascadia Code", 10))

#Position on UI
TitleLabel.grid(column=1, row=0, pady=20)
FirstCheck.grid(column=1, row=1, pady=5)
SecondCheck.grid(column=1, row=2, pady=5)
ThirdCheck.grid(column=1, row=3, pady=5)

app.mainloop()

