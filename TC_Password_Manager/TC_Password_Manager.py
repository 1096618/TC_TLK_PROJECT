import hashlib

import customtkinter
import tkinter
from tkinter import font
import sqlite3
import bcrypt
import atexit
import os
from cryptography.fernet import Fernet
import time

from PIL import Image, ImageTk
#import pyinstaller // download later


connection = sqlite3.connect('TC_Password_Manager.db')
cursor = connection.cursor()


# close db when you press x icon
def cleanup():
    connection.commit()
    connection.close()

def create_tables():
    # Connect to the SQLite database (this will create the database if it doesn't exist)
    conn = sqlite3.connect("TC_Password_Manager.db")
    cursor = conn.cursor()

    # Create 'users' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- A unique identifier for each user.
        username TEXT UNIQUE NOT NULL,         -- The username (must be unique).
        password TEXT NOT NULL,                -- The plain password (VERY ILLEGAL BUT IT PERSONAL SO DOESNT MATTER).
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
        self.geometry("480x614") #450x580
        self.title("Password Manager")
        self.resizable(False, False)

        # Call the function to set up the login page
        #self.login_page()
        self.main_menu()

    def appearance_theme(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    def login_page(self):
        # Title
        title_label = customtkinter.CTkLabel(self, text="TC Password Manager", font=("Consolas", 32),
                                             text_color="white")
        title_label.pack(padx=0, pady=50, anchor="center")

        # Login label
        login_label = customtkinter.CTkLabel(self, text="Login", font=("Consolas", 30), text_color="white")
        login_label.pack(padx=0, pady=45, anchor="center")

        # Username input
        self.username_entry = customtkinter.CTkEntry(self, placeholder_text="Username", font=("Consolas", 15)
                                                     , width=250, height=50)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Password input
        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Password", font=("Consolas", 15)
                                                     , width=250, height=50) #put show="*" later
        self.password_entry.place(relx=0.5, rely=0.56, anchor="center")

        #Create new account
        self.createaccount_label = customtkinter.CTkLabel(self, text="Create Account"
                                                          , font=("Consolas", 15, "underline")
                                                          , fg_color="transparent")
        self.createaccount_label.configure(cursor="hand2")
        self.createaccount_label.bind("<Button-1>", self.create_account_clicked)
        self.createaccount_label.place(relx=0.345, rely=0.76, anchor="center")

        # Login button
        login_button = customtkinter.CTkButton(self, text="Login", font=("Consolas", 25), width=250, height=50,
                                               command=self.login_button_pressed)
        login_button.place(relx=0.5, rely=0.67, anchor="center")


    def login_button_pressed(self):
        login_username = self.username_entry.get()
        login_password = self.password_entry.get()

        # delete error frame
        if hasattr(self, "red_frame") and self.red_frame.winfo_exists():
            self.red_frame.destroy()
        if hasattr(self, "green_frame") and self.green_frame.winfo_exists():
            self.green_frame.destroy()

        # CHECK IF INPUTTED INFO IS A VALID INPUT
        if not login_username or not login_password:
            self.show_error("Please enter all fields", width=160, relx=0.5, rely=0.94, anchor="center")
        elif len(login_username) < 3:
            self.show_error("Username too short", width=145, relx=0.5, rely=0.94, anchor="center")
        else:
            cursor.execute("SELECT password_hash FROM users WHERE username = ?", (login_username,))
            row = cursor.fetchone()

            # IF VALID IN PUT THEN BLABLA
            if row and bcrypt.checkpw(login_password.encode(), row[0].encode()):
                print("Login successful")
                self.correct_frame("Login Successful", width=160, relx=0.5, rely=0.94, anchor="center")

                self.clear_screen()
                time.sleep(3)
                self.main_menu()

            else:
                self.show_error("Invalid password or username", width=208, relx=0.5
                                                                       , rely=0.94, anchor="center")


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
        create_title_label = customtkinter.CTkLabel(self, text="TC Password Manager", font=("Consolas", 32),
                                             text_color="white")
        create_title_label.pack(padx=0, pady=50, anchor="center")

        # Create account label
        create_account_label = customtkinter.CTkLabel(self, text="Create account", font=("Consolas", 30)
                                             , text_color="white")
        create_account_label.pack(padx=0, pady=45, anchor="center")

        # Username input
        self.create_username_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Username",
            font=("Consolas", 15),
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
            font=("Consolas", 15),
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
            font=("Consolas", 15),
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
        create_account_button = customtkinter.CTkButton(self, text="Create account", font=("Consolas", 25)
                                                        , width=250
                                                        , height=50
                                                        ,command=self.create_account_button_pressed)
        create_account_button.place(relx=0.5, rely=0.78, anchor="center")

        #Switch back from create to login page
        switchx = 0.45
        switch_logintext_label = customtkinter.CTkLabel(self, text="Already have an account?"
                                                        , font=("Consolas", 15))
        switch_logintext_label.place(relx=switchx, rely=0.87, anchor="center")
        self.switch_login_label = customtkinter.CTkLabel(self, text="Log in"
                                                          , font=("Consolas", 15, "underline")
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
                                                  font=("Consolas", 15),
                                                  bg_color="transparent")
        self.error_label.place(relx=0.5, rely=0.5, anchor="center")

    def correct_frame(self, message, width=320, relx=0.5, rely=0.94, anchor="center"):
        if hasattr(self, "green_frame") and self.green_frame.winfo_exists():
            self.green_frame.destroy()

        self.green_frame = customtkinter.CTkFrame(self, width=width, height=32,
                                                  corner_radius=5, border_color="green", border_width=2)
        self.green_frame.place(relx=relx, rely=rely, anchor=anchor)

        self.success_label = customtkinter.CTkLabel(master=self.green_frame,
                                                    text=message,
                                                    font=("Consolas", 15),
                                                    bg_color="transparent")
        self.success_label.place(relx=0.5, rely=0.5, anchor="center")


    def create_account_button_pressed(self):
        print("create account button pressed")
        new_username = self.create_username_entry.get()
        new_password = self.create_password_entry.get().encode('utf-8')
        confirmed_password = self.confirm_password_entry.get().encode('utf-8')

        # delete error frame
        if hasattr(self, "red_frame") and self.red_frame.winfo_exists():
            self.red_frame.destroy()
        if hasattr(self, "green_frame") and self.green_frame.winfo_exists():
            self.green_frame.destroy()

        if not new_username or not new_password or not confirmed_password:
            self.show_error("Please enter all fields", width=160, relx=0.5, rely=0.94, anchor="center")
        elif len(new_username) < 3:
            self.show_error("Username too short", width=145, relx=0.5, rely=0.94, anchor="center")
        elif confirmed_password != new_password:
            self.show_error("Password doesnt match", width=160, relx=0.5, rely=0.94, anchor="center")
        elif len(confirmed_password) > 72: #realistically i need to make dynamic detection but this will do
            self.show_error("Password too long", width=280, relx=0.5, rely=0.94
                            , anchor="center")

        else:
            #      SALT AND HASH PASSWORD
            plain_password = self.confirm_password_entry.get()
            hashed_password = bcrypt.hashpw(confirmed_password, bcrypt.gensalt()) #salt and hash the password
            hashed_password_str = hashed_password.decode('utf-8') #convert raw byte hash pass into normal string text

            #     INPUTTING USER INFO INTO DATABASE
            try:
                with sqlite3.connect("TC_Password_Manager.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO users (username, password, password_hash) 
                        VALUES (?, ?, ?);
                    """, (new_username, plain_password, hashed_password_str))
                    conn.commit()
                    print("User registered successfully.")
                    self.correct_frame("User registered successfully.", width=208, relx=0.5, rely=0.94
                                       , anchor="center")
            except sqlite3.IntegrityError as e:
                print(f"Error: {e}")

    def main_menu(self):
        print("main menu")
        # top frame
        self.top_bar()

    def top_bar(self):
        self.top_frame = customtkinter.CTkFrame(self, width=480, height=52, fg_color="#2c2c2c", corner_radius=0)
        self.top_frame.place(relx=0.5, rely=0, anchor="n")
        
        #=========================text shennanigan============================================================
        self.text_widget = tkinter.Text(self.top_frame,
                                        font=("Consolas", 28),
                                        height=1,  # height of widget box
                                        width=40,  # width of widget box
                                        bd=0,  # border = 0 aka off
                                        highlightthickness=0,  # remove highlight border
                                        bg="#2b2b2b",  # fixed dark background
                                        fg="white",  # fixed text color
                                        insertbackground="white",  # fixed cursor color
                                        selectbackground="#555555"  # fixed selection background
                                        )
        # PLACEMENT
        self.text_widget.place(relx=0.5, rely=0.5, anchor="center")
        self.text_widget.configure(state="disabled")

        #variable for animation typing
        self.full_text = ""
        self.keyword = ""
        self.keycolor =""
        self.keyword_styles =[]
        self.current_index = 0

        #self.typing_text(text,keyword,keycolor,keyword_styles=[])
        self.typing_text("Hello User",
                         "User",
                         "green",
                         keyword_styles=["bold", "italic", "underline"]
                         )

        # =====================================================================================

        # menu icon
        menu_icon = "Assets/menu_icon2.png"  # Replace with your image file path
        pil_menu_image = Image.open(menu_icon)
        if not os.path.exists(menu_icon):
            print("Image not found:", menu_icon)

        # vault icon
        vault_icon = "Assets/vault_icon.png"  # Replace with your image file path
        pil_vault_image = Image.open(vault_icon)
        if not os.path.exists(vault_icon):
            print("Image not found:", vault_icon)

        #image object:
        #   menu object
        self.menu_icon_object = customtkinter.CTkImage(light_image=pil_menu_image, dark_image=pil_menu_image
                                                       , size=(52, 52))
        self.menu_icon = customtkinter.CTkLabel(self.top_frame, image=self.menu_icon_object, text="")
        self.menu_icon.place(relx=0, rely=0.02, anchor="nw")
        self.menu_icon.bind("<Button-1>", self.toggle_dropdown)

        #   vault object
        self.vault_icon_object = customtkinter.CTkImage(light_image=pil_vault_image, dark_image=pil_vault_image
                                                       , size=(38, 32))


        # Dropdown frame - start collapsed with height=0
        self.dropdown_frame = customtkinter.CTkFrame(self, width=52, height=0, fg_color="#2c2c2c")
        self.dropdown_frame.pack_propagate(False)  # Important: prevent auto resize
        self.dropdown_frame.place(relx=0, rely=0.08, anchor="nw")
        self.dropdown_frame.lower()

        # Add some content inside dropdown frame (hidden initially)
        self.menu_label1 = customtkinter.CTkLabel(self.dropdown_frame,image=self.vault_icon_object , text=""
                                                  , fg_color="#555555", corner_radius=5)
        self.menu_label1.bind("<Button-1>", self.toggle_dropdown)

        self.vault_label2 = customtkinter.CTkLabel(self.dropdown_frame, text="Item 2"
                                                   , fg_color="#555555", corner_radius=5)
        self.setting_label3 = customtkinter.CTkLabel(self.dropdown_frame, text="Item 3"
                                                     , fg_color="#555555", corner_radius=5)
        # Pack but initially invisible because frame height=0
        for lbl in (self.menu_label1, self.vault_label2, self.setting_label3):
            lbl.pack(fill="x", padx=10, pady=10)

        # State
        self.is_expanded = False
        self.current_height = 0
        self.target_height = 150  # final height in pixels
        self.step = 10  # pixels to expand per animation step

    def toggle_dropdown(self,event):
        if self.is_expanded:
            self.collapse()
        else:
            self.expand()

    def expand(self):
        if self.current_height < self.target_height:
            self.current_height += self.step
            if self.current_height > self.target_height:
                self.current_height = self.target_height
            self.dropdown_frame.configure(height=self.current_height)
            self.after(20, self.expand)  # call again after 20ms for smooth animation
        else:
            self.is_expanded = True
            #self.toggle_btn.configure(text="Toggle Dropdown ▲")

    def collapse(self):
        if self.current_height > 0:
            self.current_height -= self.step
            if self.current_height < 0:
                self.current_height = 0
            self.dropdown_frame.configure(height=self.current_height)
            self.after(20, self.collapse)
        else:
            self.is_expanded = False
            #self.toggle_btn.configure(text="Toggle Dropdown ▼")

    def typing_text(self,text, keyword, keycolor, keyword_styles):
        self.full_text = text
        self.keyword = keyword
        self.keycolor = keycolor
        self.keyword_styles = keyword_styles or []
        self.current_index = 0

        self.text_widget.configure(state="normal") #enable text box edit
        self.text_widget.delete("1.0", tkinter.END)
        self.text_widget.configure(state="disabled") #disabled text box edit

        # configure the font for the keyword with styles
        base_font = font.Font(font=self.text_widget["font"])
        weight = "bold" if "bold" in self.keyword_styles else "normal"
        slant = "italic" if "italic" in self.keyword_styles else "normal"
        underline = 1 if "underline" in self.keyword_styles else 0

        styled_font = font.Font(
            family=base_font.actual("family"), #get font from base font from text widget aka consolas
            size=base_font.actual("size"), #same thing as above
            weight=weight,
            slant=slant,
            underline=underline,
        )

        # Configure the highlight tag before animation starts
        self.text_widget.tag_configure("highlight", foreground=self.keycolor, font=styled_font)

        # delay till start typing
        self.after(100, self.type_next_character)

    def type_next_character(self):
        if self.current_index < len(self.full_text): #keep writing till current char match full length of text
            self.text_widget.configure(state="normal")
            next_char = self.full_text[self.current_index]
            self.text_widget.insert(tkinter.END, next_char)

            # Apply center alignment tag
            self.text_widget.tag_configure("center", justify="center")
            self.text_widget.tag_add("center", "1.0", "end")

            # Highlight keyword
            current_text = self.text_widget.get("1.0", tkinter.END) #get the full text from beginning to end text
            start = current_text.find(self.keyword) # if found keyword bind start and set it as pos of keyword else -1
            if start != -1:
                start_index = f"1.0 + {start} chars" #start index is from line 1 character 0 + pos of keyword
                end_index = f"1.0 + {start + len(self.keyword)} chars" #same thing + length
                self.text_widget.tag_remove("highlight", "1.0", tkinter.END) #remove tag if alr exist
                self.text_widget.tag_add("highlight", start_index, end_index) #add it

            self.text_widget.configure(state="disabled")
            self.current_index += 1
            self.after(100, self.type_next_character) #speed of typing animation

        else:
            self.text_widget.configure(state="disabled") #disable edit mode
            self.text_widget.configure(insertontime=0)  # hide blinking cursor
            self.text_widget.configure(cursor="arrow")  # change cursor to arrow

            # literally disabled every single cursor type when hover over text box
            self.text_widget.bind("<Button-1>", lambda e: "break")
            self.text_widget.bind("<B1-Motion>", lambda e: "break")
            self.text_widget.bind("<Double-Button-1>", lambda e: "break")
            self.text_widget.bind("<Triple-Button-1>", lambda e: "break")

    def vault_view(self,event):


# Run the app
create_tables()
atexit.register(cleanup)
app = PasswordManagerApp()
app.mainloop()
