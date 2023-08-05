import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")
        

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.pack(pady=10)

        self.amount_entry = ttk.Entry(root)
        self.amount_entry.pack(pady=5)

        self.currency_mapping = self.get_currency_mapping()

        self.from_currency_label = ttk.Label(root, text="From Currency:")
        self.from_currency_label.pack()

        self.from_currency_combo = ttk.Combobox(root, values=list(self.currency_mapping.values()), state="readonly")
        self.from_currency_combo.pack(pady=5)

        self.to_currency_label = ttk.Label(root, text="To Currency:")
        self.to_currency_label.pack()

        self.to_currency_combo = ttk.Combobox(root, values=list(self.currency_mapping.values()), state="readonly")
        self.to_currency_combo.pack(pady=5)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="", font=("Helvetica", 14, "bold"))
        self.result_label.pack()

    def get_currency_mapping(self):
        url = "https://openexchangerates.org/api/currencies.json"
        response = requests.get(url)
        currency_mapping = response.json()
        return currency_mapping

    def convert_currency(self):
        amount = float(self.amount_entry.get())
        from_currency_name = self.from_currency_combo.get()
        to_currency_name = self.to_currency_combo.get()

        from_currency_code = next(key for key, value in self.currency_mapping.items() if value == from_currency_name)
        to_currency_code = next(key for key, value in self.currency_mapping.items() if value == to_currency_name)

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency_code}"
        response = requests.get(url)
        exchange_data = response.json()
        to_currency_rate = exchange_data["rates"][to_currency_code]

        converted_amount = amount * to_currency_rate

        self.result_label.config(text=f"{amount:.2f} {from_currency_name} is equal to {converted_amount:.2f} {to_currency_name}",font=("Helvetica", 8, "bold"))

def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
