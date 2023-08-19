import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ATMGUI:
    def __init__(self, root):
        self.atm = ATM()

        self.root = root
        self.root.title("ATM Simulator")
        self.root.geometry("400x300")
        self.root.configure(bg="#f9f9f9")

        self.title_label = tk.Label(
            root, text="ATM Simulator", font=("Helvetica", 20, "bold"), bg="#f9f9f9"
        )
        self.title_label.pack(pady=10)

        self.amount_entry = tk.Entry(root, font=("Helvetica", 12))
        self.amount_entry.pack(pady=5)

        self.check_balance_button = ttk.Button(
            root, text="Check Balance", command=self.check_balance
        )
        self.check_balance_button.pack(pady=5)

        self.deposit_button = ttk.Button(
            root, text="Deposit", command=self.deposit_amount
        )
        self.deposit_button.pack(pady=5)

        self.withdraw_button = ttk.Button(
            root, text="Withdraw", command=self.withdraw_amount
        )
        self.withdraw_button.pack(pady=5)

    def check_balance(self):
        balance = self.atm.check_balance()
        self.show_balance_window(balance)

    def show_balance_window(self, balance):
        balance_window = tk.Toplevel(self.root)
        balance_window.title("Balance")
        balance_window.geometry("200x100")

        balance_label = tk.Label(
            balance_window, text=f"Your Balance: ₹{balance}", font=("Helvetica", 14)
        )
        balance_label.pack(pady=20)

    def deposit_amount(self):
        amount = float(self.amount_entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0.")
            return
        if self.atm.deposit(amount):
            self.amount_entry.delete(0, tk.END)

    def withdraw_amount(self):
        amount = float(self.amount_entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0.")
            return
        if self.atm.withdraw(amount):
            self.amount_entry.delete(0, tk.END)


class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


if __name__ == "__main__":
    root = tk.Tk()
    atm_gui = ATMGUI(root)
    root.mainloop()
