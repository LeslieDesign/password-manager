from tkinter import *
from tkinter import messagebox
import string
import secrets
import pyperclip
FONT_NAME = "Arial"
FONT_SIZE = 9

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    pwd.delete(0,END)
    pwd.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    url = website.get()
    if not url:
        messagebox.showerror("Validation Error", "Please enter a valid URL.")
    username = email.get()
    if not username:
        messagebox.showerror("Validation Error", "Please enter an email or username.")
    password = pwd.get()
    if not password:
        messagebox.showerror("Validation Error", "Please enter a password.")
    else:
        is_ok = messagebox.askokcancel(title=url, message=f"Username = {username}\nPassword = {password}\n\nIs it ok to save?")
        if is_ok:
            with open("data_file.txt", "a") as data:
                data.write(f"{url} | {username} | {password}\n")
            website.delete(0, END)
            pwd.delete(0, END)
            website.focus()


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

website = Entry(width=43)
website.focus()
website.grid(column=1, row=1, columnspan=2, sticky="w")

#Row 2:
email_lbl = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
email_lbl.grid(column=0, row=2, sticky="e")

email = Entry(width=43)
email.insert(0, "yourname@gmail.com")
email.grid(column=1, row=2, columnspan=2, sticky="w")

#Row 3:
pwd_lbl = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
pwd_lbl.grid(column=0, row=3, sticky="e")

pwd = Entry(width=23)
pwd.grid(column=1, row=3, sticky="w")

generate_btn = Button(text="Generate Password", background="azure1",
                activebackground="CadetBlue3",
                activeforeground="white", command=generate_password)
generate_btn.grid(column=1, row=3, sticky="e")

#Row 4:
add_btn = Button(text="Add to Manager", width=36, background="azure2",
                activebackground="CadetBlue3",
                activeforeground="white", command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, sticky="w")


canvas.grid(column=1, row=0)
for i in range(4):
    window.grid_rowconfigure(i, pad=3)


window.mainloop()