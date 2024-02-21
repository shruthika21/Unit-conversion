import tkinter as tk
from tkinter import ttk

def convert():
    value = float(entry.get())
    unit_from = unit_from_var.get()
    unit_to = unit_to_var.get()
    
    if unit_from == "Centimeter" and unit_to == "Feet":
        result = cm_to_feet(value)
    elif unit_from == "Feet" and unit_to == "Inches":
        result = feet_to_inches(value)
    elif unit_from == "Sqft" and unit_to == "Sqm":
        result = sqft_to_sqm(value)
    elif unit_from == "Sqft" and unit_to in ["Hectare", "Acres"]:
        result = sqft_to_hectare(value) if unit_to == "Hectare" else sqft_to_acres(value)
    else:
        result = "Invalid conversion"
    
    result_label.config(text=str(result))

root = tk.Tk()
root.title("Unit Conversion")

entry_label = tk.Label(root, text="Value:")
entry_label.grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

unit_from_label = tk.Label(root, text="From:")
unit_from_label.grid(row=1, column=0)
unit_from_var = tk.StringVar(value="Centimeter")
unit_from_menu = ttk.Combobox(root, textvariable=unit_from_var, values=["Centimeter", "Feet", "Sqft"])
unit_from_menu.grid(row=1, column=1)

unit_to_label = tk.Label(root, text="To:")
unit_to_label.grid(row=2, column=0)
unit_to_var = tk.StringVar(value="Feet")
unit_to_menu = ttk.Combobox(root, textvariable=unit_to_var, values=["Feet", "Inches", "Sqm", "Hectare", "Acres"])
unit_to_menu.grid(row=2, column=1)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
