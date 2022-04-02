from tkinter import *
# PASSWORD MANAGER


# SAVE PASSWORD


# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=300)
lock_img = PhotoImage(file="./logo.png")
canvas.create_image(150, 150, image=lock_img)
canvas.grid()

window.mainloop()
