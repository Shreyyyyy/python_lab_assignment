import tkinter as tk
from tkinter import messagebox
import re

# Function to validate input using regular expressions
def validate_input(widget, regex, error_message):
    user_input = widget.get()
    if re.match(regex, user_input):
        return True
    else:
        messagebox.showerror("Validation Error", error_message)
        return False

# Function to handle form submission
def submit_form():
    # Validate and get input values
    airline_name = entry_name.get()
    airline_id_valid = validate_input(entry_id, r'^[0-9]+$', "Invalid Airline ID")
    alias = entry_alias.get()
    iata_valid = validate_input(entry_iata, r'^[A-Z0-9]+$', "Invalid IATA Code")
    icao_valid = validate_input(entry_icao, r'^[A-Z0-9]+$', "Invalid ICAO Code")
    callsign_valid = validate_input(entry_callsign, r'^[A-Za-z0-9\s]+$', "Invalid Callsign")
    country = option_var.get()
    active = active_var.get()
    
    # Perform a simple calculation (e.g., age from DOB)
    # Here, we'll just print the input values and perform a dummy calculation
    print(f"Airline Name: {airline_name}")
    if airline_id_valid:
        print(f"Airline ID: {entry_id.get()}")
    print(f"Alias: {alias}")
    if iata_valid:
        print(f"IATA Code: {entry_iata.get()}")
    if icao_valid:
        print(f"ICAO Code: {entry_icao.get()}")
    if callsign_valid:
        print(f"Callsign: {entry_callsign.get()}")
    print(f"Country: {country}")
    print(f"Active: {active}")
    
    # You can perform further calculations or actions as needed
    
# Create the main window
root = tk.Tk()
root.title("Airline Management System Form")

# Create and arrange widgets

# Labels
label_name = tk.Label(root, text="Airline Name:")
label_id = tk.Label(root, text="Airline ID:")
label_alias = tk.Label(root, text="Alias:")
label_iata = tk.Label(root, text="IATA Code:")
label_icao = tk.Label(root, text="ICAO Code:")
label_callsign = tk.Label(root, text="Callsign:")
label_country = tk.Label(root, text="Country:")
label_active = tk.Label(root, text="Active:")

# Entry widgets
entry_name = tk.Entry(root)
entry_id = tk.Entry(root)
entry_alias = tk.Entry(root)
entry_iata = tk.Entry(root)
entry_icao = tk.Entry(root)
entry_callsign = tk.Entry(root)

# OptionMenu (Dropdown)
countries = ["United States", "Canada", "United Kingdom", "Australia", "France"]
option_var = tk.StringVar(root)
option_var.set(countries[0])  # Set the default value
option_menu = tk.OptionMenu(root, option_var, *countries)

# Checkbutton (Active/Inactive)
active_var = tk.StringVar()
active_checkbutton = tk.Checkbutton(root, text="Active", variable=active_var, onvalue="Y", offvalue="N")

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)

# Arrange widgets using grid layout
label_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
label_id.grid(row=1, column=0)
entry_id.grid(row=1, column=1)
label_alias.grid(row=2, column=0)
entry_alias.grid(row=2, column=1)
label_iata.grid(row=3, column=0)
entry_iata.grid(row=3, column=1)
label_icao.grid(row=4, column=0)
entry_icao.grid(row=4, column=1)
label_callsign.grid(row=5, column=0)
entry_callsign.grid(row=5, column=1)
label_country.grid(row=6, column=0)
option_menu.grid(row=6, column=1)
label_active.grid(row=7, column=0)
active_checkbutton.grid(row=7, column=1)
submit_button.grid(row=8, columnspan=2)

# Start the GUI event loop
root.mainloop()