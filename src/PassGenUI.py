import tkinter as tk
from tkinter import messagebox
from PassGen import addParameters, generatePassword

## Anthony Varela, 2026
## Personal project and my first Python project.
## This module provides the graphical interface for PassGen using Tkinter.
## It allows users to choose a password length and character types,
## generate passwords, and display validation messages.
## The password-generation logic is handled by the password_generator module.

## Function that triggers everything once the Generate button is pressed. First we make sure the input for 
## the length is right and it;s a number, if it;s not it will show either two errors. We get the values of the
## check boxes and make sure there is at least one selected. Finally we call the other two functions and 
## insert the password in the generatedPassEntry field.
def generate():

    try:
        length_val = int(length.get())
        if length_val < 12 or 60 < length_val:
            messagebox.showerror("Error length", "Password must be between 12 and 60 characters")
            return
    except ValueError:
        messagebox.showerror("Incorrect input", "Please insert a number")
        return

    upper_val = upper.get()
    lower_val = lower.get()
    num_val = num.get()
    chars_val = chars.get()

    if not upper_val and not lower_val and not num_val and not chars_val:
        messagebox.showerror("No options selected", "You have to select at least one option as yes!")
        return

    pswd, lochars = addParameters(upper_val, lower_val, num_val, chars_val)
    final = generatePassword(pswd, length_val, lochars)
    generatedPassEntry.delete(0, 'end')
    generatedPassEntry.insert(0, final)

## Function that copies the password to the clipboard.
def copy():
    password = generatedPassEntry.get()
    if password != "":
        window.clipboard_clear()
        window.clipboard_append(password)

## Function that clears all the fields in the GUI.
def clear():
    length.delete(0, 'end')
    upper.set(False)
    lower.set(False)
    num.set(False)
    chars.set(False)
    generatedPassEntry.delete(0, 'end')

## Main window creation and configuration.
#########################################################################
window = tk.Tk()
window.title("PassGen")
window.geometry("600x400")
window.iconbitmap("C:/Users/antho/Downloads/PassGenIcon.ico")
window.configure(bg="#1d3354")
#########################################################################

## First block with the label and the entry for the desired password length
#########################################################################
length_label = tk.Label(
    window,
    text="Password Length",
    font="palatino",
    bg="#9ed8db"
)
length_label.pack()

length = tk.Entry(window, bg="#9ed8db")
length.pack(padx=10, pady= 10)
#########################################################################

## Second block containing all the boolean variables from the checkboxes. Organize in using Frames
#########################################################################
upper =  tk.BooleanVar()
lower =  tk.BooleanVar()
num = tk.BooleanVar()
chars = tk.BooleanVar()

checkboxFrame = tk.Frame(bg="#9ed8db")
checkboxFrame.pack(pady=10)

tk.Checkbutton(
    checkboxFrame,
    text="Uppercase letters",
    font="palatino",
    bg="#d64045",
    variable=upper
).grid(row=0, column= 0, padx=10, pady= 5, sticky="w")

tk.Checkbutton(
    checkboxFrame,
    text="Lowercase letters",
    font="palatino",
    bg="#d64045",
    variable=lower
).grid(row=0, column= 1, padx=10, pady= 5, sticky="w")

tk.Checkbutton(
    checkboxFrame,
    text="Numbers",
    font="palatino",
    bg="#d64045",
    variable=num
).grid(row=1, column= 0, padx=10, pady= 5, sticky="w")

tk.Checkbutton(
    checkboxFrame,
    text="Special characters",
    font="palatino",
    bg="#d64045",
    variable=chars
).grid(row=1, column= 1, padx=10, pady= 5, sticky="w")
#########################################################################

## Third block with the button generate password.
#########################################################################
generateButton = tk.Button(
    window, 
    text="Generate password",
    font="palatino",
    bg="#d64045",
    command=generate
).pack()
#########################################################################

## Fourth block containing the label and the field with the generated password.
#########################################################################
resultbox = tk.Frame(bg="#9ed8db")
resultbox.pack(pady=15)

genpasslabel = tk.Label(
    resultbox,
    text="Generated password:",
    bg="#9ed8db",
    font="palatino",
)
genpasslabel.grid(row=0, column= 0, padx=0, pady= 0, sticky="w")

generatedPassEntry = tk.Entry(resultbox, bg="#9ed8db")
generatedPassEntry.grid(row=1, column= 0, padx=0, pady= 0, sticky="w")
#########################################################################

## Last block containing the copy and clear buttons.
#########################################################################
commandbox = tk.Frame(bg="#1d3354")
commandbox.pack(pady=20)

copybutton = tk.Button(
    commandbox,
    text="Copy",
    bg="#9ed8db",
    font="palatino",
    command=copy
).grid(row=0, column= 0, padx=10, pady= 0, sticky="w")

generateButton = tk.Button(
    commandbox, 
    text="Clear",
    font="palatino",
    bg="#e9fff9",
    command=clear
).grid(row=0, column= 1, padx=10, pady= 0, sticky="w")
#########################################################################

## Activates the window.
window.mainloop()