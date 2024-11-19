-- Create table for storing enquiries
CREATE TABLE enquiries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    salutation TEXT,
    address TEXT,
    phone TEXT,
    cemetery_name TEXT,
    fixing_area TEXT,
    enquiry_status TEXT,
    followup_notes TEXT,
    date_created TEXT,
    date_closed TEXT,
    reason_for_closure TEXT
);
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database connection setup
def connect_db():
    conn = sqlite3.connect("memorial.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enquiries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact_name TEXT,
            salutation TEXT,
            address TEXT,
            phone TEXT,
            cemetery_name TEXT,
            fixing_area TEXT,
            enquiry_status TEXT,
            followup_notes TEXT,
            date_created TEXT,
            date_closed TEXT,
            reason_for_closure TEXT
        )
    """)
    conn.commit()
    conn.close()

# Main App
class MemorialManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memorial Management System")
        self.geometry("1200x800")
        connect_db()

        # Header
        self.create_header()

        # Tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Adding Tabs
        self.general_details_tab = GeneralDetailsTab(self.notebook)
        self.notebook.add(self.general_details_tab, text="General Details")

    def create_header(self):
        header_frame = tk.Frame(self, bg="lightgrey")
        header_frame.pack(fill="x")

        # Add buttons for header
        buttons = ["Create NEW Enquiry", "Refresh", "Edit", "Clear", "Print", "Search", "Save Enquiry", "Convert", "Exit"]
        for btn_text in buttons:
            tk.Button(header_frame, text=btn_text, padx=10, pady=5, command=self.on_button_click).pack(side="left", padx=5, pady=5)

    def on_button_click(self):
        # Placeholder for button actions
        messagebox.showinfo("Info", "Button clicked!")

class GeneralDetailsTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Enquiry Details Section
        tk.Label(self, text="Enquiry Details", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        
        tk.Label(self, text="Contact Name:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.contact_name_entry = tk.Entry(self, width=30)
        self.contact_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Salutation:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.salutation_entry = tk.Entry(self, width=30)
        self.salutation_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text="Address:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.address_entry = tk.Entry(self, width=50)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text="Telephone Number:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.telephone_entry = tk.Entry(self, width=20)
        self.telephone_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self, text="Cemetery Name:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.cemetery_name_entry = tk.Entry(self, width=30)
        self.cemetery_name_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self, text="Fixing Area:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.fixing_area_entry = tk.Entry(self, width=30)
        self.fixing_area_entry.grid(row=6, column=1, padx=5, pady=5)

        # Save Button
        tk.Button(self, text="Save Enquiry", command=self.save_enquiry).grid(row=7, column=0, columnspan=2, pady=10)

    def save_enquiry(self):
        contact_name = self.contact_name_entry.get()
        salutation = self.salutation_entry.get()
        address = self.address_entry.get()
        phone = self.telephone_entry.get()
        cemetery_name = self.cemetery_name_entry.get()
        fixing_area = self.fixing_area_entry.get()

        if not contact_name or not address:
            messagebox.showerror("Error", "Please fill all required fields!")
            return

        conn = sqlite3.connect("memorial.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO enquiries (contact_name, salutation, address, phone, cemetery_name, fixing_area, date_created)
            VALUES (?, ?, ?, ?, ?, ?, DATE('now'))
        """, (contact_name, salutation, address, phone, cemetery_name, fixing_area))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Enquiry saved successfully!")
        self.clear_form()

    def clear_form(self):
        self.contact_name_entry.delete(0, tk.END)
        self.salutation_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.telephone_entry.delete(0, tk.END)
        self.cemetery_name_entry.delete(0, tk.END)
        self.fixing_area_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = MemorialManagementApp()
    app.mainloop()
