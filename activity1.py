import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        root.title("Restaurant Management App")
        root.geometry("500x500")
    
        self.menu = {
            "FRIES MEAL":2, "LUNCH MEAL":2,
            "BURGER MEAL":3, "PIZZA MEAL":4,
            "CHEESE BURGER":2.5, "DRINKS":1
        }
        self.rate = 93
        self.entries = {}
        self.labels = {}
        frame = ttk.Frame(root, padding=15)
        frame.place(relx = 0.5, rely = 0.5, anchor = "center")
        ttk.Label(frame, text = "Restaurtant Order Managment", font = ("Arial", 16, "bold")).grid(row=0,columnspan=2,pady=10)
        for i, (item, price) in enumerate(self.menu.items(), 1):
            label = ttk.Label(frame)
            label.grid(row=i, column=0, padx=10, pady=5)
            self.labels[item]=label

            entry = ttk.Entry(frame, width=6)
            entry.grid(row=i,column=1)
            self.entries[item] = entry

        self.currency = tk.StringVar(value="USD")
        ttk.Label(frame, text="Currency: ").grid(row=7,column=0)
        ttk.Combobox(frame, textvariable=self.currency, values = ["USD", "INR"], state="readonly").grid(row=7, column=1)

        self.currency.trace_add("write", self.update_prices)
        self.update_prices()
        ttk.Button(frame, text="Place Order", command=self.place_order).grid(row=8, columnspan=2, pady=10)

    def update_prices(self, *args):
        rate = self.rate if self.currency.get()=="INR" else 1
        symbol = "₹" if self.currency.get() == "INR" else "$"

        for item, label in self.labels.items():
            label.config(text=f"{item} ({symbol}{self.menu[item]*rate}): ")
    def place_order(self):
        rate = self.rate if self.currency.get() == "INR" else 1
        symbol = "₹" if self.currency.get() == "INR" else "$"
        total, summary = 0, "Order Summary: "

        for item, entry in self.entries.items():
            try:
                qty = int(entry.get() or 0)
                if qty < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Enter valid quantities.")
                return

            price = self.menu[item]*rate
            cost = qty * price
            total += cost
            if qty:
                summary += f"{item}: {qty} x {symbol}{price} = {symbol}{cost}"
        if total:
            messagebox.showinfo("Order Placed", summary + f"Total: {symbol}{total}")
        else:
            messagebox.showerror("Error", "Order at least one item.")
root = tk.Tk()
app = RestaurantOrderManagement(root)
root.mainloop()