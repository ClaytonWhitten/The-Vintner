# This is the Vintner App for winemakers.
# @author Clayton Whitten

from tkinter import *
import customtkinter
from PIL import Image
import sys
import os

customtkinter.set_default_color_theme("dark-blue")

def grav_to_brix(SG):
    brix = (((182.4601 * SG - 775.6821) * SG + 1262.7794) * SG - 669.5622)
    rounded_brix = round(brix, 2)
    return rounded_brix

def tosna_calculation():
    pass

app = customtkinter.CTk()


app.geometry('800x600')
app.iconbitmap(default='custom_assets/bottle.ico')
app.title('The Vintner')

top_frame = customtkinter.CTkFrame(
    app,
    fg_color='white',
    width=800,
    height=100,
    corner_radius=0
)
top_frame.pack(pady=20)

logo = customtkinter.CTkImage(
    light_image=Image.open("custom_assets/logo.png"),
    dark_image=Image.open("custom_assets/darkmode_logo.png"),
    size=(315, 61.6)
)

logo_label = customtkinter.CTkLabel(
    top_frame,
    image=logo,
    text=None,
    anchor='w'
)
logo_label.pack()

tosna_button = customtkinter.CTkButton(
    app,
    text='Tailored Organic Staggered Nutrient Addition Calculator', # Tailored Organic Staggered Nutrient Addition
    font=customtkinter.CTkFont(family='Aldrich', size=14),
    fg_color='#0050FF',
    corner_radius=10
)
tosna_button.pack()


app.mainloop()

