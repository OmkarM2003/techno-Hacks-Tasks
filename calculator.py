import tkinter as tk

def on_click(btn_text):
    if btn_text == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif btn_text == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, btn_text)

# Create the main window
root = tk.Tk()
root.title("Visually Pleasing Calculator")
root.geometry("375x645")
root.configure(bg="#f0f0f0")

# Create the display
display = tk.Entry(root, width=15, font=('Helvetica', 30), borderwidth=5, relief=tk.RIDGE, bg="#fff")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Define button labels and colors
button_data = [
    ("7", "#3c3c3c"), ("8", "#3c3c3c"), ("9", "#3c3c3c"), ("/", "#db5f3d"),
    ("4", "#3c3c3c"), ("5", "#3c3c3c"), ("6", "#3c3c3c"), ("*", "#db5f3d"),
    ("1", "#3c3c3c"), ("2", "#3c3c3c"), ("3", "#3c3c3c"), ("-", "#db5f3d"),
    ("0", "#3c3c3c"), (".", "#3c3c3c"), ("=", "#55ae5e"), ("+", "#db5f3d"),
    ("C", "#c03c3c")
]

# Create and place buttons
row = 1
col = 0
for label, color in button_data:
    button = tk.Button(root, text=label, padx=20, pady=20, font=('Helvetica', 20),
                       command=lambda lbl=label: on_click(lbl), bg=color, fg="#fff", relief=tk.FLAT)
    button.grid(row=row, column=col, padx=5, pady=5, ipadx=2, ipady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main loop
root.mainloop()
