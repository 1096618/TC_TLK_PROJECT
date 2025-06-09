import customtkinter as ctk
import sqlite3
import tkinter as tk
from tkinter import messagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class VaultApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("480x614")
        self.title("Password Vault")

        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.create_sample_data()

        self.selected_entry = None

        # Split layout
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.left_panel = ctk.CTkFrame(self.main_frame, width=180)
        self.left_panel.pack(side="left", fill="y", padx=5, pady=5)

        self.right_panel = ctk.CTkFrame(self.main_frame)
        self.right_panel.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        self.create_left_list()
        self.create_detail_view()

    class AccountBlock(ctk.CTkFrame):
        def __init__(self, parent, account_data, conn, refresh_callback=None):
            super().__init__(parent)
            self.conn = conn
            self.cursor = conn.cursor()
            self.account_data = account_data
            self.refresh_callback = refresh_callback
            self.expanded = False

            self.toggle_btn = ctk.CTkButton(self, text=account_data[1],  # Username as label
                                            command=self.toggle_details)
            self.toggle_btn.pack(fill="x")

            self.details_frame = ctk.CTkFrame(self)
            self.create_detail_widgets()

        def create_detail_widgets(self):
            _, name, website, password, notes, updated = self.account_data

            self.entries = {}

            for label_text, value in [
                ("Username", name),
                ("Password", password),
                ("Notes", notes),
                ("Updated", updated)
            ]:
                label = ctk.CTkLabel(self.details_frame, text=label_text + ":")
                label.pack(anchor="w", padx=10, pady=(5, 0))
                entry = ctk.CTkEntry(self.details_frame, width=250)
                entry.insert(0, value)
                entry.pack(padx=10, pady=2)
                self.entries[label_text.lower()] = entry

            self.save_btn = ctk.CTkButton(self.details_frame, text="Save", command=self.save_changes)
            self.save_btn.pack(pady=5)

            self.delete_btn = ctk.CTkButton(self.details_frame, text="Delete", fg_color="red",
                                            command=self.delete_entry)
            self.delete_btn.pack()

        def toggle_details(self):
            if self.expanded:
                self.details_frame.pack_forget()
            else:
                self.details_frame.pack(fill="x", pady=5)
            self.expanded = not self.expanded

        def save_changes(self):
            user_id = self.account_data[0]
            updated_data = (
                self.entries["username"].get(),
                self.account_data[2],  # website unchanged
                self.entries["password"].get(),
                self.entries["notes"].get(),
                self.entries["updated"].get(),
                user_id
            )

            self.cursor.execute("""
                UPDATE users SET name = ?, website = ?, password = ?, notes = ?, updated_at = ? WHERE id = ?
            """, updated_data)
            self.conn.commit()

            messagebox.showinfo("Saved", "Account updated.")
            if self.refresh_callback:
                self.refresh_callback()

        def delete_entry(self):
            confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this account?")
            if confirm:
                self.cursor.execute("DELETE FROM users WHERE id = ?", (self.account_data[0],))
                self.conn.commit()
                self.destroy()
                if self.refresh_callback:
                    self.refresh_callback()

    def create_sample_data(self):
        self.cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                website TEXT,
                password TEXT,
                notes TEXT,
                updated_at TEXT
            );
        """)
        sample_users = [
            (1, "Alice", "gmail.com", "password123", "Personal email", "2025-06-01"),
            (2, "Dice", "gmail.com", "password132", "work email", "2025-05-01"),
            (3, "Bob", "github.com", "devpass", "Work repos", "2025-06-01"),
            (4, "Charlie", "bank.com", "securepass!", "Bank login", "2025-06-01")
        ]
        self.cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", sample_users)
        self.conn.commit()

    def create_left_list(self):
        self.entry_list_frame = ctk.CTkScrollableFrame(self.left_panel)
        self.entry_list_frame.pack(fill="both", expand=True)

        self.refresh_entry_list()

    def refresh_entry_list(self):
        for widget in self.entry_list_frame.winfo_children():
            widget.destroy()

        self.cursor.execute("SELECT DISTINCT website FROM users")
        websites = self.cursor.fetchall()

        for website_tuple in websites:
            website = website_tuple[0]
            button = ctk.CTkButton(self.entry_list_frame, text=website,
                                   command=lambda w=website: self.show_accounts_for_website(w),
                                   anchor="w", width=160)
            button.pack(pady=4, padx=5)

    def create_detail_view(self):
        # Right panel now holds a scrollable frame where we insert collapsible account blocks
        self.account_container = ctk.CTkScrollableFrame(self.right_panel)
        self.account_container.pack(fill="both", expand=True, padx=10, pady=10)

    def show_accounts_for_website(self, website):
        # Clear the right panel
        for widget in self.account_container.winfo_children():
            widget.destroy()

        self.cursor.execute("SELECT * FROM users WHERE website = ?", (website,))
        accounts = self.cursor.fetchall()

        for acc in accounts:
            block = self.AccountBlock(self.account_container, acc, self.conn, refresh_callback=self.refresh_entry_list)
            block.pack(fill="x", pady=5, padx=5)

    def save_changes(self):
        if not self.selected_entry:
            return

        user_id = self.selected_entry[0]
        updated_data = (
            self.inputs["username"].get(),
            self.inputs["website"].get(),
            self.inputs["password"].get(),
            self.inputs["notes"].get(),
            self.inputs["updated"].get(),
            user_id
        )

        self.cursor.execute("""
            UPDATE users SET name = ?, website = ?, password = ?, notes = ?, updated_at = ? WHERE id = ?
        """, updated_data)
        self.conn.commit()

        messagebox.showinfo("Saved", "Changes saved successfully.")
        self.refresh_entry_list()

    def delete_entry(self):
        if not self.selected_entry:
            return

        user_id = self.selected_entry[0]
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this entry?")
        if confirm:
            self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            self.conn.commit()
            self.selected_entry = None

            # Clear detail fields
            for entry in self.inputs.values():
                entry.delete(0, tk.END)

            self.refresh_entry_list()



app = VaultApp()
app.mainloop()
