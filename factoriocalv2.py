from tkinter import *

class UI:
    def __init__(self, wantpersec, crafttime, assemblerswitch, needassembler, manypercraft):
        self.wantpersec = StringVar()
        self.crafttime = StringVar()
        self.assemblerswitch = StringVar()
        self.needassembler = StringVar()
        self.manypercraft = StringVar()

def start_calculating(ui):
    try:
        if float(ui.manypercraft.get()) == 0: 
            RealCraftTime = float(ui.crafttime.get()) / float(ui.assemblerswitch.get())
            ItemsPerSec = 1 / RealCraftTime
            result = float(ui.wantpersec.get()) / ItemsPerSec
            ui.needassembler.set(result)
        else:
            RealCraftTime = float(ui.crafttime.get()) / float(ui.assemblerswitch.get())
            ItemsPerSec = 1 / RealCraftTime
            result = float(ui.wantpersec.get()) / ItemsPerSec
            result = result * float(ui.manypercraft.get())
            ui.needassembler.set(result)
    except ZeroDivisionError as e:
         print(e)

def main():
    root = Tk()
    root.geometry('400x150')
    ui = UI(StringVar,StringVar,StringVar,StringVar, StringVar)
    ui.manypercraft.set(0)

    def enter_button():
        start_calculating(ui)
    
    want_label = Label(root, text='How much is wanted per second?')
    want_entry = Entry(root, textvariable=ui.wantpersec)

    crafttime_label = Label(root, text='How long to craft item?')
    crafttime_entry = Entry(root, textvariable=ui.crafttime)

    manypercraft_label = Label(root, text ='How much is made per craft?')
    manypercraft_entry = Entry(root, textvariable=ui.manypercraft)

    assemb_1 = Radiobutton(root, text='Assembler 1', variable=ui.assemblerswitch, value=.5)
    assemb_2 = Radiobutton(root, text='Assembler 2', variable=ui.assemblerswitch, value=.75)
    assemb_3 = Radiobutton(root, text='Assembler 3', variable=ui.assemblerswitch, value=1.25)

    enter_btn = Button(root, text='Enter', command=enter_button)

    needassemb_label = Label(root, text='Amount of assemblers needed.')
    needassemb_entry= Entry(root, textvariable=ui.needassembler)

    want_label.grid(row=0, column=1)
    want_entry.grid(row=0, column=0)

    crafttime_label.grid(row=1, column=1)
    crafttime_entry.grid(row=1, column=0)

    manypercraft_label.grid(row=2, column=1)
    manypercraft_entry.grid(row=2, column=0)

    assemb_1.grid(row=3, column=0)
    assemb_2.grid(row=3, column=1)
    assemb_3.grid(row=3, column=2)

    enter_btn.grid(row=4, column=1)

    needassemb_label.grid(row=5, column=1)
    needassemb_entry.grid(row=5, column=0)

    root.mainloop()

main()