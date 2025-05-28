import customtkinter
import sqlite3
import bcrypt
from cryptography.fernet import Fernet


connection = sqlite3.connect('TC_Password_Manager.db')
cursor = connection.cursor()


def create_tables():
    # Connect to the SQLite database (this will create the database if it doesn't exist)
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()

    # Create 'users' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- A unique identifier for each user.
        username TEXT UNIQUE NOT NULL,         -- The username (must be unique).
        password_hash TEXT NOT NULL,           -- The hashed version of the user's password.
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP  -- Automatically records when the account was created.
    );""")

    # Create 'vault_entries' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vault_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- A unique identifier for each vault entry.
        user_id INTEGER NOT NULL,              -- The ID of the user who owns this entry (foreign key).
        website TEXT NOT NULL,                 -- The website or service (e.g., 'gmail.com').
        username TEXT NOT NULL,                -- The username for the website/service.
        password_encrypted TEXT NOT NULL,      -- The encrypted password for the website.
        notes TEXT,                            -- Optional notes for additional information.
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Automatically records when the entry was created.
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Automatically records when the entry was last updated.
        FOREIGN KEY (user_id) REFERENCES users(id)  -- Ensures this entry belongs to a valid user.
    );""")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class PasswordManagerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # App thing
        self.geometry("450x580")
        self.title("Password Manager")
        self.resizable(False, False)

        # Call the function to set up the login page
        self.login_page()

    def appearance_theme(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    def login_page(self):
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


    def login_button_pressed(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Username entered: {username}")
        print(f"Password entered: {password}")
        if username == "test" and password == "test123":
            print("correct username and password entered")
            if hasattr(self, "red_frame") and self.red_frame.winfo_exists(): #if red frame exist delete
                self.red_frame.destroy(), self.invalid_pass.destroy()

        else:
            #     create red frame and label saying invalid password
            self.red_frame = customtkinter.CTkFrame(self, width=150, height=32
                                                    , corner_radius=5, border_color="red", border_width=2)
            self.red_frame.place(relx=0.5, rely=0.94, anchor="center")
            self.invalid_pass =customtkinter.CTkLabel(master = self.red_frame, text="Invalid password"
                                                      , font=("Comic Sans MS", 15), bg_color="transparent")
            self.invalid_pass.place(relx=0.5, rely=0.5, anchor="center")

    def create_account_clicked(self, event):
        print("create new account clicked")
        self.clear_screen()
        #self.create_account_page() #bug test
        self.after(0, self.create_account_page)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_account_page(self):
        # Create Title
        create_title_label = customtkinter.CTkLabel(self, text="TC Password Manager", font=("Comic Sans MS", 32),
                                             text_color="white")
        create_title_label.pack(padx=0, pady=50, anchor="center")

        # Create account label
        create_account_label = customtkinter.CTkLabel(self, text="Create account", font=("Comic Sans MS", 30)
                                             , text_color="white")
        create_account_label.pack(padx=0, pady=45, anchor="center")

        # Username input
        self.create_username_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Username",
            font=("Comic Sans MS", 15),
            width=250,
            height=50,
            fg_color="#2b2b2b",
            text_color="white",
            placeholder_text_color="gray70"
        )
        self.create_username_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Password input
        self.create_password_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Password",
            font=("Comic Sans MS", 15),
            width=250,
            height=50,
            fg_color="#2b2b2b",
            text_color="white",
            placeholder_text_color="gray70"
        )
        self.create_password_entry.place(relx=0.5, rely=0.56, anchor="center")

        # Confirm Password input
        self.confirm_password_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Confirm password",
            font=("Comic Sans MS", 15),
            width=250,
            height=50,
            fg_color="#2b2b2b",
            text_color="white",
            placeholder_text_color="gray70"
        )
        self.confirm_password_entry.place(relx=0.5, rely=0.67, anchor="center")

        # Force placeholder render on username field
        #self.create_username_entry.focus()
        #self.create_password_entry.update()  # Shift focus to another field
        #self.confirm_password_entry.update()
        #self.update_idletasks()
        self.focus()    # Return focus to the root window

        # Create account button
        create_account_button = customtkinter.CTkButton(self, text="Create account", font=("Comic Sans MS", 25)
                                                        , width=250
                                                        , height=50
                                                        ,command=self.create_account_button_pressed)
        create_account_button.place(relx=0.5, rely=0.78, anchor="center")

        #Switch back from create to login page
        switchx = 0.45
        switch_logintext_label = customtkinter.CTkLabel(self, text="Already have an account?"
                                                        , font=("Comic Sans MS", 15))
        switch_logintext_label.place(relx=switchx, rely=0.87, anchor="center")
        self.switch_login_label = customtkinter.CTkLabel(self, text="Log in"
                                                          , font=("Comic Sans MS", 15, "underline")
                                                          , fg_color="transparent")
        self.switch_login_label.configure(cursor="hand2")
        self.switch_login_label.bind("<Button-1>", self.switch_login_clicked)
        self.switch_login_label.place(relx=switchx+0.235, rely=0.87, anchor="center")

    def switch_login_clicked(self, event):
        print("switch login clicked")
        self.clear_screen()
        self.login_page()

    def show_error(self, message, width=320, relx=0.5, rely=0.94, anchor="center"):
        if hasattr(self, "red_frame") and self.red_frame.winfo_exists():
            self.red_frame.destroy()

        self.red_frame = customtkinter.CTkFrame(self, width=width, height=32,
                                                corner_radius=5, border_color="red", border_width=2)
        self.red_frame.place(relx=relx, rely=rely, anchor=anchor)

        self.error_label = customtkinter.CTkLabel(master=self.red_frame,
                                                  text=message,
                                                  font=("Comic Sans MS", 15),
                                                  bg_color="transparent")
        self.error_label.place(relx=0.5, rely=0.5, anchor="center")

    def create_account_button_pressed(self):
        print("create account button pressed")
        new_username = self.create_username_entry.get()
        new_password = self.create_password_entry.get().encode('utf-8')
        confirm_password = self.confirm_password_entry.get().encode('utf-8')

        if not new_username or not new_password or not confirm_password:
            self.show_error("Please enter all fields", width=160, relx=0.5, rely=0.94, anchor="center")
        elif len(new_username) < 3:
            self.show_error("Username too short", width=145, relx=0.5, rely=0.94, anchor="center")



# Run the app
app = PasswordManagerApp()
app.mainloop()
