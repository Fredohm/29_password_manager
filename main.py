from tkinter import *
# PASSWORD MANAGER


# SAVE PASSWORD


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

username_entry = Entry(width=55)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, pady=2)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
