# This is the Vintner App for winemakers.
# @author Clayton Whitten

from tkinter import *
from tkinter.font import *
import customtkinter
import sys

def grav_to_brix(SG):
    brix = (((182.4601 * SG - 775.6821) * SG + 1262.7794) * SG - 669.5622)
    rounded_brix = round(brix, 2)
    return rounded_brix

def tosna_calculation():
    pass

window = Tk()


window.configure(bg='black')
w_icon = PhotoImage(file='bottle.png')
window.iconphoto(False, w_icon)
window.geometry('800x600')
window.title('The Vintner')


intro = Label(
    window,
    text='The Vintner: Organize Your Wines',
    foreground='blue',
    background='black',
    font=('Bahnschrift SemiBold', 26),
    anchor='center',
)
intro.pack(pady=40)

nutrients = ['Fermaid O', 'Fermaid K']

nutrient_preference = OptionMenu(
    window,

)

batch_size_label = Label(
    window,
    text='Batch Size (In Gallons)',
    background='black',
    foreground='white'
)
batch_size_label.pack(pady=5)
batch_size_entry = Entry(window)
batch_size_entry.pack()

tosna_button = Button(
    window,
    text='TOSNA 3.0 Calculator',
    fg='white',
    bg='#FF0000',
    width=20,
    command=lambda: print('new window')
)
button_font = Font(family='Yu Gothic', weight='bold')
tosna_button['font'] = button_font
tosna_button.pack(pady=20)


window.mainloop()

