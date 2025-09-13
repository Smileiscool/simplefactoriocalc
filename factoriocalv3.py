from tkinter import *

class UI:
    def __init__(self, wantpersec, crafttime, assemblerswitch, needassembler, manypercraft):
        self.wantpersec = DoubleVar()
        self.crafttime = DoubleVar()
        self.assemblerswitch = DoubleVar()
        self.needassembler = DoubleVar()
        self.manypercraft = DoubleVar()

def start_calculating(ui):
    try:
        RealCraftTime = float(ui.crafttime.get()) / float(ui.assemblerswitch.get())
        ItemsPerSec = 1 / RealCraftTime
        result = float(ui.wantpersec.get()) / ItemsPerSec
        ui.needassembler.set(result)
        try:
            if float(ui.manypercraft.get()) > 0:
                result = result * float(ui.manypercraft.get())
                ui.needassembler.set(result)
        except: 
            print('How many per craft set to invalid.')
    except:
         print('Main Calc Error')

def main():
    root = Tk()
    root.geometry('400x150')
    ui = UI(DoubleVar, DoubleVar, DoubleVar, DoubleVar, DoubleVar)

    ui.assemblerswitch.set(1.25)

    def calc_button():
        start_calculating(ui)

    def clear_button():
        ui.wantpersec.set(0)
        ui.crafttime.set(0)
        ui.manypercraft.set(0)
        ui.assemblerswitch.set(1.25)
        ui.needassembler.set(0)

    def on_key_press(event):
        if event.keysym == 'Return':
            start_calculating(ui)
        else:
            pass

    want_label = Label(root, text='How much is wanted per second?')
    want_entry = Entry(root, textvariable=ui.wantpersec)

    crafttime_label = Label(root, text='How long to craft item?')
    crafttime_entry = Entry(root, textvariable=ui.crafttime)

    manypercraft_label = Label(root, text ='How much is made per craft?')
    manypercraft_entry = Entry(root, textvariable=ui.manypercraft)

    assemb_1 = Radiobutton(root, text='Assembler 1', variable=ui.assemblerswitch, value=.5)
    assemb_2 = Radiobutton(root, text='Assembler 2', variable=ui.assemblerswitch, value=.75)
    assemb_3 = Radiobutton(root, text='Assembler 3', variable=ui.assemblerswitch, value=1.25)

    calc_btn = Button(root, text='Enter', command=calc_button)

    clear_btn = Button(root, text='Clear', command=clear_button)

    needassemb_label = Label(root, text='Amount of assemblers needed.')
    needassemb_entry= Entry(root, textvariable=ui.needassembler)

    root.bind("<KeyPress>", on_key_press)

    want_label.grid(row=0, column=1)
    want_entry.grid(row=0, column=0)

    crafttime_label.grid(row=1, column=1)
    crafttime_entry.grid(row=1, column=0)

    manypercraft_label.grid(row=2, column=1)
    manypercraft_entry.grid(row=2, column=0)

    assemb_1.grid(row=3, column=0)
    assemb_2.grid(row=3, column=1)
    assemb_3.grid(row=3, column=2)

    calc_btn.grid(row=4, column=1)

    clear_btn.grid(row=4, column=0)

    needassemb_label.grid(row=5, column=1)
    needassemb_entry.grid(row=5, column=0)

    root.mainloop()

main()