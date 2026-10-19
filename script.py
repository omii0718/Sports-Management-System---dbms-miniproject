import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Database Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="om"
)

cursor = con.cursor()

# Main Window
root = tk.Tk()
root.title("Sports Management System")
root.geometry("750x550")
root.configure(bg="#EAF2F8")

tk.Label(
    root,
    text="SPORTS MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#1B2631",
    fg="white",
    pady=15
).pack(fill="x")

# Input Fields
form = tk.Frame(root, bg="#EAF2F8")
form.pack(pady=15)

fields = ["Staff ID", "Staff Name", "Address", "Role"]
entries = []

for i, field in enumerate(fields):
    tk.Label(
        form,
        text=field,
        font=("Arial", 11),
        bg="#EAF2F8",
        width=12,
        anchor="w"
    ).grid(row=i, column=0, padx=10, pady=5)

    entry = tk.Entry(form, width=30, font=("Arial", 11))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

id_entry, name_entry, address_entry, role_entry = entries


# INSERT
def insert_staff():
    try:
        values = (
            id_entry.get().strip(),
            name_entry.get().strip(),
            address_entry.get().strip(),
            role_entry.get().strip()
        )

        if not all(values):
            messagebox.showwarning("Warning", "Fill all fields")
            return

        query = """
            INSERT INTO staff (s_id, s_name, s_address, s_role)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, values)
        con.commit()

        messagebox.showinfo(
            "Success", "Staff inserted successfully!"
        )
        retrieve_staff()

    except mysql.connector.Error as e:
        con.rollback()
        messagebox.showerror("Database Error", str(e))


# RETRIEVE
def retrieve_staff():
    try:
        for item in tree.get_children():
            tree.delete(item)

        cursor.execute(
            "SELECT s_id, s_name, s_address, s_role FROM staff"
        )

        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))


# SELECT A RECORD
def select_staff(event):
    selected = tree.selection()

    if not selected:
        return

    values = tree.item(selected[0], "values")

    for entry, value in zip(entries, values):
        entry.delete(0, tk.END)
        entry.insert(0, value)


# UPDATE
def update_staff():
    try:
        staff_id = id_entry.get().strip()
        name = name_entry.get().strip()
        address = address_entry.get().strip()
        role = role_entry.get().strip()

        if not all([staff_id, name, address, role]):
            messagebox.showwarning("Warning", "Fill all fields")
            return

        query = """
            UPDATE staff
            SET s_name = %s, s_address = %s, s_role = %s
            WHERE s_id = %s
        """

        cursor.execute(
            query, (name, address, role, staff_id)
        )

        if cursor.rowcount == 0:
            con.rollback()
            messagebox.showwarning(
                "Not Found", "Staff ID not found"
            )
            return

        con.commit()

        messagebox.showinfo(
            "Success", "Staff updated successfully!"
        )
        retrieve_staff()

    except mysql.connector.Error as e:
        con.rollback()
        messagebox.showerror("Database Error", str(e))


# DELETE
def delete_staff():
    staff_id = id_entry.get().strip()

    if not staff_id:
        messagebox.showwarning(
            "Warning", "Enter or select a Staff ID"
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        f"Delete staff record with ID {staff_id}?"
    )

    if not confirm:
        return

    try:
        cursor.execute(
            "DELETE FROM staff WHERE s_id = %s",
            (staff_id,)
        )

        if cursor.rowcount == 0:
            con.rollback()
            messagebox.showwarning(
                "Not Found", "Staff ID not found"
            )
            return

        con.commit()

        messagebox.showinfo(
            "Success", "Staff deleted successfully!"
        )
        retrieve_staff()

    except mysql.connector.Error as e:
        con.rollback()
        messagebox.showerror(
            "Database Error",
            "Could not delete the record.\n" + str(e)
        )


# BUTTONS
button_frame = tk.Frame(root, bg="#EAF2F8")
button_frame.pack(pady=10)

buttons = [
    ("Insert", insert_staff),
    ("Update", update_staff),
    ("Delete", delete_staff),
    ("Retrieve / Refresh", retrieve_staff)
]

for i, (text, command) in enumerate(buttons):
    tk.Button(
        button_frame,
        text=text,
        command=command,
        width=14,
        bg="#2874A6",
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2"
    ).grid(row=0, column=i, padx=4, pady=5)


# DISPLAY RECORDS
tree_frame = tk.Frame(root)
tree_frame.pack(fill="both", expand=True, padx=15, pady=10)

columns = ("ID", "Name", "Address", "Role")

tree = ttk.Treeview(
    tree_frame,
    columns=columns,
    show="headings",
    height=7
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=160, anchor="center")

tree.pack(fill="both", expand=True)

tree.bind("<<TreeviewSelect>>", select_staff)

# Display existing staff records
retrieve_staff()

# Run Application
root.mainloop()