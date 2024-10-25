import tkinter as tk
from tkinter import messagebox

def regular_notes():
    try:
        # Logic to find the correct beat number
        beats_per_measure = int(entry_num1.get())
        type_of_note = int(entry_num2.get())

        whole = type_of_note
        half = whole / 2
        quarter = half / 2
        eith = quarter / 2
        sixteenth = eith /2

        # output text
        output = (
            f"Whole note: {whole} beat(s)\n"
            f"Half note: {half} beat(s)\n"
            f"Quarter note: {quarter} beat(s)\n"
            f"Eighth note: {eith} beat(s)\n"
            f"Sixteenth note: {sixteenth} beat(s)"
        )

        label_result.config(text=output)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def dotted_notes():
    try:
        # Logic to find the correct beat number
        beats_per_measure = int(entry_num1.get())
        type_of_note = int(entry_num2.get())

        whole = type_of_note
        half = whole / 2
        quarter = half / 2
        eith = quarter / 2
        sixteenth = eith /2

        # output text
        output = (
            f"Whole note: {(whole) * 1.5} beat(s)\n"
            f"Half note: {(half) * 1.5} beat(s)\n"
            f"Quarter note: {(quarter)* 1.5} beat(s)\n"
            f"Eighth note: {(eith) * 1.5} beat(s)\n"
            f"Sixteenth note: {(sixteenth) * 1.5} beat(s)"
        )
        label_result.config(text=output)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def triplets():
    try:
        # Logic to find the correct beat number
        beats_per_measure = int(entry_num1.get())
        type_of_note = int(entry_num2.get())

        # Implement the triplet logic
        whole = type_of_note

        quarter_triplet = beats_per_measure - 2

        # output text
        output = (
            f"Whole note: {-0} beat(s)\n"
            f"Half note: {-0} beat(s)\n"
            f"Quarter note: {-0} beat(s)\n"
            f"Eighth note: {-0} beat(s)\n"
            f"Sixteenth note: {-0} beat(s)"
        )
        label_result.config(text=output)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("MUSC 2024 Beat Calculator")
root.geometry("400x275")  # Set window size

# Create and place the widgets
label_num1 = tk.Label(root, text="# of beats per measure:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="type of note that gets a count:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

button_regular = tk.Button(button_frame, text="Regular note", command=regular_notes)
button_regular.pack(side=tk.LEFT)

button_dotted = tk.Button(button_frame, text="Dotted note", command=dotted_notes)
button_dotted.pack(side=tk.LEFT)

button_triplet = tk.Button(button_frame, text="Triplet", command=triplets)
button_triplet.pack(side=tk.LEFT)

label_result = tk.Label(root, text="Beats: ")
label_result.pack()

# Run the application
root.mainloop()
