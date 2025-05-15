from tkinter import *
import customtkinter

#APPEARANCE AND THEME
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#APP NAME AND RESOLUTION
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("450x580")
app.title("Password Manager")

#FONT
#title_font = customtkinter.CTkFont("Comic Sans MS", 32)

#--------------------------------------------LOGIN PAGE------------------------------------------------------#

#Title
title_label = customtkinter.CTkLabel(app, text="TC Password Manager", font=("Comic Sans MS",32), text_color="white")
title_label.pack(padx=0, pady=50, anchor="center")

login_label = customtkinter.CTkLabel(app, text="Login", font=("Comic Sans MS",30), text_color="white")
title_label.pack(padx=0, pady=50, anchor="center")


def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
login_button = customtkinter.CTkButton(master=app, text="CTkButton",width= 250, height= 50, command=button_function)
login_button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

app.mainloop()