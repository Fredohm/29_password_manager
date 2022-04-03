from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# PASSWORD MANAGER
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    generated_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# SAVE PASSWORD
def save():
    website = website_input.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {username}\n"
                                                              f"Password: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            with open("./password_list.txt", mode="a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                password_entry.delete(0, END)


# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=5)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, pady=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5)

# Entries
website_input = Entry(width=55)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_entry = Entry(width=55)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "fredohm@hutmail.bu")

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, pady=2, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
