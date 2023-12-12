from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for char in range(randint(8, 10))]
    password_symbols=[choice(symbols) for char in range(randint(2, 4))]
    password_numbers=[choice(numbers) for char in range(randint(2, 4))]

    password_list=password_numbers+password_symbols+password_letters

    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    e_mail = email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
            "e-mail": e_mail,
            "password": password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="Empty Spaces",message="Dont Leave Any Empty Spaces")
    else:
        try:
            with open("data.json", mode="r") as file:
                #Reading old data
                data=json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                #Saving Updated Data
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                #Saving Updated Data
                json.dump(data,file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
def search():
    website=website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
            pyperclip.copy(data[website]['password'])
            messagebox.showinfo(title="Site Info",
                                message=f"Site:{website}\n"
                                        f"E-Mail:{data[website]['e-mail']}\n"
                                        f"Password:{data[website]['password']}"
                                        f"Password copied in clipboar")
        else:
            messagebox.showinfo(title="Error",message=f"There is no website called {website} in saved passwords ")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "berkay@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()