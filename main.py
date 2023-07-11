# This is the Vintner App for winemakers.
# @author Clayton Whitten
import tkinter.font
from tkinter import *
from tkinter.font import *
import customtkinter
from PIL import Image
import sys
import os


# Multiple screens script taken from here:
# https://stackoverflow.com/questions/70165908/how-to-switch-screens-using-tkinter

def clear_frame():
    for widget in app.winfo_children():
        widget.destroy()


def syna_screen():
    clear_frame()

    top_frame = customtkinter.CTkFrame(
        app,
        fg_color='transparent',
        border_width=1,
        border_color='white',
        corner_radius=0
    )
    top_frame.pack(side=TOP, fill='x')

    back_button = customtkinter.CTkButton(
        top_frame,
        text="Go Back",
        font=main_font,
        fg_color='#0065FF',
        corner_radius=10,
        command=lambda: main_screen(),
    )
    back_button.pack(padx=20, pady=10, side=LEFT)

    syna_label = customtkinter.CTkLabel(
        top_frame,
        text="Staggered Yeast Nutrient Addition",
        font=customtkinter.CTkFont(family="Aldrich", size=28),
        text_color='#0065FF',
        anchor='center',
    )
    syna_label.pack(padx=20, pady=10, side=LEFT)

    middle_frame = customtkinter.CTkFrame(
        app,
        fg_color='transparent',
    )
    middle_frame.pack(pady=20, fill='x')

    syna_text = customtkinter.CTkTextbox(
        middle_frame,
        wrap='word',
        border_width=1,
        border_color='white'
    )
    syna_text.insert("0.0", "The Staggered Yeast Nutrient Addition is a formula"
                     " that calculates how much yeast nutrient should be added at"
                     " specific time intervals throughout the fermentation process."
                     " All calculations are done assuming you use one 5 gram packet of yeast per gallon.")
    syna_text.tag_config("center", justify='center')
    syna_text.configure(state="disabled", font=main_font, text_color='white', height=50, width=800, fg_color='transparent')
    syna_text.pack(padx=20)


    batch_unit_text = customtkinter.CTkTextbox(app)
    batch_unit_text.insert("0.0", "Batch Measurement:")
    batch_unit_text.tag_config("center", justify='center')
    batch_unit_text.configure(state="disabled", font=("Aldrich", 12), text_color='white', height=10, fg_color='transparent')
    batch_unit_text.pack()

    batch_units = ['Gallons', 'Liters']
    batch_unit_selection = customtkinter.CTkOptionMenu(
        app,
        values=batch_units,
        font=main_font,
        anchor='center'
    )
    batch_unit_selection.pack()

    batch_size_entry = customtkinter.CTkEntry(
        app,
        placeholder_text='Enter Batch Size:'
    )
    batch_size_entry.pack(pady=(10, 20))

    yeast_selection_text = customtkinter.CTkTextbox(app)
    yeast_selection_text.insert("0.0", "Yeast Selection:")
    yeast_selection_text.tag_config("center", justify='center')
    yeast_selection_text.configure(state="disabled", font=("Aldrich", 12), text_color='white', height=10, fg_color='transparent')
    yeast_selection_text.pack()

    yeast_options = ['Lalvin EC-1118', 'Lalvin 71B', 'Lalvin K1-V1116', 'Lalvin QA23', 'Lalvin D-47']
    yeast_selection = customtkinter.CTkOptionMenu(
        app,
        values=yeast_options,
        font=main_font
    )
    yeast_selection.pack(pady=(0, 10))

    starting_gravity_text = customtkinter.CTkTextbox(app)
    starting_gravity_text.insert("0.0", "Starting Gravity:")
    starting_gravity_text.tag_config("center", justify='center')
    starting_gravity_text.configure(state="disabled", font=("Aldrich", 12), text_color='white', height=10, fg_color='transparent')
    starting_gravity_text.pack(pady=(10, 0))

    starting_gravity_entry = customtkinter.CTkEntry(
        app,
        placeholder_text='(Example: 1.050):'
    )
    starting_gravity_entry.pack(pady=(0, 10))

    fruit_gravity_text = customtkinter.CTkTextbox(app)
    fruit_gravity_text.insert("0.0", "Fruit Gravity (Optional):")
    fruit_gravity_text.tag_config("center", justify='center')
    fruit_gravity_text.configure(state="disabled", font=("Aldrich", 12), text_color='white', height=10, fg_color='transparent')
    fruit_gravity_text.pack(pady=(10, 0))

    fruit_gravity_entry = customtkinter.CTkEntry(
        app,
        placeholder_text='Enter Fruit Gravity:'
    )
    fruit_gravity_entry.pack(pady=(0, 20))

    calculate_button = customtkinter.CTkButton(
        app,
        text='Calculate SYNA',
        font=main_font,
        command=lambda: show_answer(syna_calculation(yeast_selection.get(), batch_unit_selection.get(),
                                         batch_size=batch_size_entry.get(), starting_gravity=starting_gravity_entry.get(),
                                         fruit_gravity=fruit_gravity_entry.get())),
        corner_radius=10,
        fg_color="#0065FF"
    )
    calculate_button.pack()

    # function to show the answer
def show_answer(syna_calc):
    answer_level = customtkinter.CTkToplevel(app)
    answer_level.iconbitmap('custom_assets/bottle.ico')
    answer_level.title("Staggered Yeast Nutrient Addition Calculation")
    answer_level.geometry("600x400")
    answer_level.attributes('-topmost', 'true')
    calculation_text = customtkinter.CTkLabel(
        answer_level,
        text=f'Add {syna_calc} grams of Fermaid-O at 24, 48, and 72 hours, and then at the 7 day mark',
        font=customtkinter.CTkFont(family='Aldrich', size=18),
        text_color='#0065FF',
        wraplength=200
    )
    calculation_text.pack()


def main_screen():
    clear_frame()

    logo = customtkinter.CTkImage(
        light_image=Image.open("custom_assets/logo.png"),
        dark_image=Image.open("custom_assets/darkmode_logo.png"),
        size=(315, 61.6)
    )

    logo_label = customtkinter.CTkLabel(
        app,
        image=logo,
        text=None,
    )
    logo_label.pack(pady=20)

    syna_button = customtkinter.CTkButton(
        app,
        text='SYNA Calculator',
        font=main_font,
        fg_color='#0065FF',
        corner_radius=10,
        command=lambda: syna_screen(),
    )
    syna_button.pack(pady=20)


# converts specific gravity measurement of water into Brix measurement
def to_brix(specific_gravity):
    brix = (((182.4601 * specific_gravity - 775.6821) * specific_gravity + 1262.7794) * specific_gravity - 669.5622)
    rounded_brix = round(brix, 2)
    return rounded_brix

# finds nitrogen requirement of yeast
def n_requirement(yeast):
    match yeast:
        case 'Lalvin EC-1118':
            return 0.15
        case 'Lalvin 71B':
            return 0.15
        case 'Lalvin K1-V1116':
            return 0.15
        case 'Lalvin QA23':
            return 0.15
        case 'Lalvin D-47':
            return 0.15
        case _:
            return -1


# Staggered Yeast Nutrient Addition
def syna_calculation(yeast_type, unit_of_measure, batch_size, starting_gravity, fruit_gravity=''):
    new_fruit = 0
    starting_gravity = float(starting_gravity)
    if fruit_gravity != 0 and fruit_gravity.isdigit():
        new_fruit = float(fruit_gravity)
        new_fruit = new_fruit - 1
    elif fruit_gravity.isalnum():
        new_fruit = 0
    brix = to_brix(starting_gravity + new_fruit)
    nitrogen_demand = n_requirement(yeast_type)
    if nitrogen_demand == -1:
        return "Please select a yeast"
    if unit_of_measure == 'Liters':
        batch_size = round((batch_size * 0.264), 2)
    grams_fermaid_o = brix * nitrogen_demand * float(batch_size)
    nutrient_addition = round((grams_fermaid_o / 4.0), 1)
    return nutrient_addition

# End Of Functions



app = customtkinter.CTk()

customtkinter.set_default_color_theme("dark-blue")
customtkinter.FontManager.load_font("custom_assets/Aldrich-Regular.ttf")
main_font = customtkinter.CTkFont(family="Aldrich", size=14)


app.geometry('800x600')
app.iconbitmap('custom_assets/bottle.ico')
app.title('The Vintner')


main_screen()
app.mainloop()
