from tkinter import *

FONT_NAME = "Calibri"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Window set up
window = Tk()
window.title("Password Manger")
# window.minsize(width=240, height=240)
window.config(padx=20, pady=20)

# Canvas set up
canvas = Canvas(width=200, height=200)

# Add logo
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Label - website
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# Entry - website input
web_input = Entry(width=36)
web_input.grid(column=1, row=1, columnspan=2)

# Label - email/username
usr_label = Label(text="Email/Username:")
usr_label.grid(column=0, row=2)

# Entry - email/username input
usr_input = Entry(width=36)
usr_input.grid(column=1, row=2, columnspan=2)

# Label - password
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

# Entry - password input
pw_input = Entry(width=21)
pw_input.grid(column=1, row=3)


# Buttons
# Generate password
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

# Add
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
