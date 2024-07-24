from tkinter import *
import datetime
from tkinter import messagebox
import random
import pyperclip
import pandas

#----------------------------create file---------------------------------#
def create_file():
    with open("password_manager.csv", 'w') as file:
        file.write("Website,Email,Password,Time\n")


#-----------------------------------search-------------------------------#
def search():

    data = pandas.read_csv("password_manager.csv")
    web = web_entry.get()
    if web == '':
        messagebox.showwarning(title="Warning", message="please fill website item!")
    else:
        try:
            data_web = data[data.Website == web]
            full_data = data_web.values
            messagebox.showinfo(message=f"Website: {full_data[0][0]}\nEmail: {full_data[0][1]}\n"
                                        f"Password: {full_data[0][2]}\nTime: {full_data[0][3]}")
        except:
            messagebox.showwarning(title="Error", message=f"Dont Have {web} Data in Database")

        finally:
            web_entry.delete(0, END)
            pas_entry.delete(0, END)
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
                                 message=f"Website: {web}\nEmail: {gmail}\nPassword: {password}")

        if ok:
            messagebox.showinfo(title="Congratulations", message="Details were recorded!")
            try:
                with open("password_manager.csv", 'r') as file_r:
                    file_r.read()
            except FileNotFoundError:
                create_file()
                with open("password_manager.csv", 'a') as file:
                    file.write(f"{web},{gmail},{password},{datetime.datetime.now()} \n")

            finally:
                web_entry.delete(0, END)
                pas_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0,)
canvas.create_image(50, 100, image=img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website")
web_label.grid(column=0, row=1)
web_entry = Entry(width=21)
web_entry.grid(column=1, row=1, sticky="W")
web_entry.focus()

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
email_entry = Entry(width=37)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_entry.insert(0, "example@gmail.com")

pas_label = Label(text="Password")
pas_label.grid(column=0, row=3)
pas_entry = Entry(width=21)
pas_entry.grid(column=1, row=3, sticky="W")
pas_button = Button(text="Generate Password", command=gen_password)
pas_button.grid(column=1, row=3, sticky="E")

add_button = Button(text="Add", width=32, command=save)
add_button.grid(column=1, row=4)

search_button = Button(text="search", command=search, width=14)
search_button.grid(column=1, row=1, sticky="E")


window.mainloop()