from tkinter import *
from tkinter import messagebox
from password import generator
import pyperclip
import json

FONT_NAME = "Calibri"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def fill_password():
    gen_password = generator()
    pw_input.insert(0, gen_password)
    pyperclip.copy(gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_input.get().title()
    usr = usr_input.get()
    pw = pw_input.get()

    # create new dict for data storage
    new_data = {
        website: {
            "email": usr,
            "password": pw,
        }
    }

    # Validate no empty fields, warn user if field empty
    if not website or not pw:
        messagebox.showinfo(title="Missing Field(s)", message="Oh no! You left something blank.")

    else:
        # Check details and confirm save in messagebox
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {usr} \n"
                                                              f"Password: {pw} \nIs it ok to save?")

        # changing file type to json file, separate read/write
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Create file and write to file
                    json.dump(new_data, file, indent=4)

            else:
                # Updating old data w new data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

            finally:
                # clear website / pw fields
                web_input.delete(0, END)
                pw_input.delete(0, END)


# ---------------------------- SEARCH PASSWORDS ------------------------------- #

def search():
    website = web_input.get().title()

    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found.\nClick OK to start adding passwords")
    else:
        try:
            email_lu = data[website]["email"]
            pass_lu = data[website]["password"]

            messagebox.showinfo(title=website, message=f"Email: {email_lu} \nPassword: {pass_lu}")

        except KeyError:
            messagebox.showinfo(title="Add password?", message=f"No credentials found for {website}.\nClick OK to add")




# ---------------------------- UI SETUP ------------------------------- #
# Window set up
window = Tk()
window.title("Password Manger")
# window.minsize(width=240, height=240)
window.config(padx=50, pady=50)


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
web_input = Entry(width=21)
web_input.grid(column=1, row=1, sticky="E", padx=20)
# call focus so cursor starts in entry field
web_input.focus()


# Label - email/username
usr_label = Label(text="Email/Username:")
usr_label.grid(column=0, row=2)

# Entry - email/username input
usr_input = Entry(width=43)
usr_input.grid(column=1, row=2, columnspan=2, sticky="E")
# Populate entry field
usr_input.insert(0, "ksg.dev.data@gmail.com")

# Label - password
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

# Entry - password input
pw_input = Entry(width=21)
pw_input.grid(column=1, row=3, sticky="e", padx=20)


# Buttons
# Generate password
generate_button = Button(text="Generate Password", command=fill_password)
generate_button.grid(column=2, row=3, sticky="E")

# Add
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="E")

# Search button
search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=2, row=1, sticky="E")

window.mainloop()