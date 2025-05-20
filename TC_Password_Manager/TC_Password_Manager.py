import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class PasswordManagerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # App thing
        self.geometry("450x580")
        self.title("Password Manager")

        # Call the function to set up the login page
        self.create_login_page()

    def create_login_page(self):
        # Title
        title_label = customtkinter.CTkLabel(self, text="TC Password Manager", font=("Comic Sans MS", 32),
                                             text_color="white")
        title_label.pack(padx=0, pady=50, anchor="center")

        # Login label
        login_label = customtkinter.CTkLabel(self, text="Login", font=("Comic Sans MS", 30), text_color="white")
        login_label.pack(padx=0, pady=45, anchor="center")

        # Username input
        self.username_entry = customtkinter.CTkEntry(self, placeholder_text="Username", font=("Comic Sans MS", 15)
                                                     , width=250, height=50)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Password input
        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Password", font=("Comic Sans MS", 15)
                                                     , width=250, height=50)
        self.password_entry.place(relx=0.5, rely=0.56, anchor="center")

        #Create new account
        self.createaccount_label = customtkinter.CTkLabel(self, text="Create Account"
                                                          , font=("Comic Sans MS", 15, "underline")
                                                          , fg_color="transparent")
        self.createaccount_label.configure(cursor="hand2")
        self.createaccount_label.bind("<Button-1>", self.create_account_clicked)
        self.createaccount_label.place(relx=0.335, rely=0.76, anchor="center")

        # Login button
        login_button = customtkinter.CTkButton(self, text="Login", font=("Comic Sans MS", 25), width=250, height=50,
                                               command=self.login_button_pressed)
        login_button.place(relx=0.5, rely=0.67, anchor="center")

    def create_account_clicked(self, event):
        print("create new account clicked")

    def login_button_pressed(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Username entered: {username}")
        print(f"Password entered: {password}")

# Run the app
app = PasswordManagerApp()
app.mainloop()
