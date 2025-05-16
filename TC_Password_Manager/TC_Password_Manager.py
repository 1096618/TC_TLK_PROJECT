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
        login_label.pack(padx=0, pady=46, anchor="center")

        # Username input
        #self.username_input = customtkinter.CTkTextbox(self, width=250, height=50)
        #self.username_input.place(relx=0.5, rely=0.47, anchor="center")

        username_label = customtkinter.CTkLabel(self, text="", font=("Comic Sans MS", 30),)
        username_label.pack(pady=46)

        username_entry = customtkinter.CTkEntry(self, placeholder_text="Username")
        username_entry.place(relx=0.5, rely=0.47, anchor="center")

        # Login button
        login_button = customtkinter.CTkButton(self, text="Login", font=("Comic Sans MS", 25), width=250, height=50,
                                               command=self.login_button_pressed)
        login_button.place(relx=0.5, rely=0.8, anchor="center")

    def login_button_pressed(self):
        # Handle the login button press
        print(f"Username entered: {self.username_input.get('1.0', 'end-1c')}")
        # Add login logic here


# Run the app
app = PasswordManagerApp()
app.mainloop()
