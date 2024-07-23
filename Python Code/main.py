from tkinter import *
import datetime
from tkinter import messagebox
import random
import pyperclip

#setup time for password
with open("password_manager.csv", 'a') as file:
    file.write(f"\n\nTIME: ({datetime.datetime.now()})\n\n")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    #create random passwor
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pas_letter = [letters[x] for x in range(random.randint(8, 10))]
    pas_num = [numbers[x] for x in range(random.randint(2, 4))]
    pas_sym = [symbols[x] for x in range(random.randint(2, 4))]

    password_list = pas_letter + pas_num + pas_sym

    random.shuffle(password_list)

    password = "".join(password_list)

    pas_entry.delete(0, END)
    pas_entry.insert(0, password)

#copy password
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #save password on csv file
    web = web_entry.get()
    gmail = email_entry.get()
    password = pas_entry.get()
    #check fild
    if web == '' or gmail == '' or password == '':
        messagebox.showwarning(title="Warning", message="Please fill in all items!!!")

    else:
        #check items
        ok = messagebox.askyesno(title="Do You Want To Save?",
                                 message=f"Website: {web}\n Email: {gmail}\n Password: {password}")

        if ok:
            messagebox.showinfo(title="Congratulations", message="Details were recorded!")
            with open("password_manager.csv", 'a') as file:
                file.write(f"Website: {web} | Email: {gmail} | Password: {password} \n")
            web_entry.delete(0, END)
            pas_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0,)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website")
web_label.grid(column=0, row=1)
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@gmail.com")

pas_label = Label(text="Password")
pas_label.grid(column=0, row=3)
pas_entry = Entry(width=21)
pas_entry.grid(column=1, row=3)
pas_button = Button(text="Generate Password", command=gen_password)
pas_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()