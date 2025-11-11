from tkinter import *
from tkinter import messagebox
import string
import secrets
import pyperclip
import json
FONT_NAME = "Arial"
FONT_SIZE = 9

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    pwd_entry.delete(0,END)
    pwd_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    username = email.get()
    password = pwd_entry.get()
    new_data = {
        website: {
            "email" : username,
            "password" : password
        }
    }

    if not password or not website:
        messagebox.showerror("Validation Error", "Please make sure no fields are empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pwd_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=260, height=260, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(125,125, image=logo_img)

#Row 1:
website_lbl = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
website_lbl.grid(column=0, row=1, sticky="e")

website_entry = Entry(width=23)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="ew", padx=5)

search_btn = Button(text="Search", background="azure1", width=15,
                activebackground="CadetBlue3",
                activeforeground="white", command=find_password)
search_btn.grid(column=2, row=1, sticky="e")

#Row 2:
email_lbl = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
email_lbl.grid(column=0, row=2, sticky="w")

email = Entry(width=30)
email.insert(0, "yourname@gmail.com")
email.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5)

#Row 3:
pwd_lbl = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
pwd_lbl.grid(column=0, row=3, sticky="e")

pwd_entry = Entry(width=23)
pwd_entry.grid(column=1, row=3, sticky="ew", padx=5)

generate_btn = Button(text="Generate Password", background="azure1", width=15,
                activebackground="CadetBlue3",
                activeforeground="white", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="w")

#Row 4:
add_btn = Button(text="Add to Manager", width=36, background="black", fg="white",
                activebackground="CadetBlue3",
                activeforeground="white", command=save_data)
add_btn.grid(column=1, row=4, columnspan=3, sticky="ew", pady=10)


canvas.grid(column=1, row=0)
for i in range(4):
    window.grid_rowconfigure(i, pad=4)

window.mainloop()