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

    def create_account_clicked(self, event):
        print("create new account clicked")
        self.appearance_theme()
        self.clear_screen()
        self.create_account_page()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_account_page(self):
        # Title
        title_label = customtkinter.CTkLabel(self, text="TC Password Manager", font=("Comic Sans MS", 32),
                                             text_color="white")
        title_label.pack(padx=0, pady=50, anchor="center")

        # Login label
        login_label = customtkinter.CTkLabel(self, text="Create account", font=("Comic Sans MS", 30)
                                             , text_color="white")
        login_label.pack(padx=0, pady=45, anchor="center")

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

        self.create_username_entry.update()
        self.create_password_entry.update()
        self.confirm_password_entry.update()

# Run the app
app = PasswordManagerApp()
app.mainloop()
