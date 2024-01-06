import tkinter as tk
from tkinter import messagebox

class JewelryManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Jewelry Management System")

        # Variables
        self.inventory = []

        # Labels
        tk.Label(master, text="Jewelry Management System", font=('Helvetica', 16)).grid(row=0, column=1, pady=10)

        # Entry Widgets
        tk.Label(master, text="Jewelry Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(master, text="Quantity:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(master, text="Add Jewelry", command=self.add_jewelry).grid(row=3, column=1, pady=10)
        tk.Button(master, text="View Inventory", command=self.view_inventory).grid(row=4, column=1, pady=10)

    def add_jewelry(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()

        if name and quantity:
            try:
                quantity = int(quantity)
                self.inventory.append({"Name": name, "Quantity": quantity})
                messagebox.showinfo("Success", "Jewelry added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Quantity must be a number.")
        else:
            messagebox.showerror("Error", "Please enter both name and quantity.")

    def view_inventory(self):
        if not self.inventory:
            messagebox.showinfo("Inventory", "Inventory is empty.")
        else:
            inventory_text = "Jewelry Inventory:\n"
            for item in self.inventory:
                inventory_text += f"{item['Name']}: {item['Quantity']} pieces\n"
            messagebox.showinfo("Inventory", inventory_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = JewelryManagementSystem(root)
    root.mainloop()
