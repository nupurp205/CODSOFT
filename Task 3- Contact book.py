import tkinter as tk
from tkinter import ttk, messagebox

# List to store contacts
contacts = []

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    refresh_contacts()
    clear_entries()

# Refresh the contact list in Treeview
def refresh_contacts():
    contact_list.delete(*contact_list.get_children())
    for i, contact in enumerate(contacts):
        contact_list.insert('', 'end', iid=i, values=(
            contact["name"], contact["phone"], contact["email"], contact["address"]
        ))

# Search for contacts
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(*contact_list.get_children())
    for i, contact in enumerate(contacts):
        if query in contact["name"].lower() or query in contact["phone"]:
            contact_list.insert('', 'end', iid=i, values=(
                contact["name"], contact["phone"], contact["email"], contact["address"]
            ))

# Populate entry fields when a contact is selected
def on_select(event):
    selected = contact_list.focus()
    if selected:
        contact = contacts[int(selected)]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact["address"])

# Update a contact
def update_contact():
    selected = contact_list.focus()
    if selected:
        index = int(selected)
        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        refresh_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Select a contact to update.")

# Delete a contact
def delete_contact():
    selected = contact_list.focus()
    if selected:
        result = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if result:
            contacts.pop(int(selected))
            refresh_contacts()
            clear_entries()
    else:
        messagebox.showwarning("Warning", "Select a contact to delete.")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("📒 Contact Book")
root.state("zoomed")  # Maximize the window

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Labels and Entry Fields
tk.Label(input_frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(input_frame, width=40)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Phone").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(input_frame, width=40)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(input_frame, width=40)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Address").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(input_frame, width=40)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Contact", width=15, bg="green", fg="white", command=add_contact).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Update Contact", width=15, bg="blue", fg="white", command=update_contact).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Delete Contact", width=15, bg="red", fg="white", command=delete_contact).grid(row=0, column=2, padx=10)

# Search Bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
search_entry = tk.Entry(search_frame, width=40)
search_entry.grid(row=0, column=0, padx=5)
tk.Button(search_frame, text="Search", command=search_contact).grid(row=0, column=1, padx=5)

# Treeview for contact list
columns = ("Name", "Phone", "Email", "Address")
contact_list = ttk.Treeview(root, columns=columns, show='headings')

# Define headings and column width
for col in columns:
    contact_list.heading(col, text=col)
    contact_list.column(col, anchor="center", stretch=True, width=250)

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=contact_list.yview)
contact_list.configure(yscroll=scrollbar.set)

# Pack Treeview and scrollbar
contact_list.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Bind selection
contact_list.bind('<<TreeviewSelect>>', on_select)

# Run the app
root.mainloop()
