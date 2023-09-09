from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Times New Roman", 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    t3.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = t1.get()
    password = t3.get()
    email = t2.get()
    new_data = {
        web: {
            "Password": password,
            "Email": email
        }
    }

    if len(web) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="ALERT", message="All the fields must be filled !")

    else:

        go = messagebox.askokcancel(title=web, message=f"You have entered:\nEmail: {email}\nWebsite: {web}\nPassword: {password}\nDo you wish to save it ?")

        if go:
            try:
                with open("data.json", "r") as file:
                    # Reading the old data
                    data = json.load(file)

            except FileNotFoundError:

                with open("data.json", "w") as file:
                    # Creating new JSON file
                    json.dump(new_data, file, indent=4)

            else:
                # Updating the data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            t1.delete(0, "end")
            t2.delete(0, "end")
            t3.delete(0, "end")
            t1.focus()


# ---------------------------- SEARCHING ENTRIES ------------------------------- #
def search():
    try:
        with open("data.json", "r") as file:
            # Reading the old data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(text="Oops", message="No Data File Found")

    else:
        web = t1.get()

        if web in data:
            messagebox.showinfo(title=web, message=f"Email: {data[web]['Email']}\nPassword: {data[web]['Password']}")
        else:
            messagebox.showwarning(title="Notice", message="This entry does not exist!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

l1 = Label(text="Website:", font=FONT)
l1.grid(column=0, row=1)

l2 = Label(text="Email/Username:", font=FONT)
l2.grid(column=0, row=2)

l3 = Label(text="Password:", font=FONT)
l3.grid(column=0, row=3)

t1 = Entry(width=21)
t1.grid(column=1, row=1)
t1.focus()

t2 = Entry(width=35)
t2.grid(column=1, row=2, columnspan=2)
t2.insert(0, "mymailid@demo.com")

t3 = Entry(width=21)
t3.grid(column=1, row=3)

b1 = Button(text="Generate Password", command=pw)
b1.grid(column=2, row=3)

b2 = Button(text="Add", width=36, command=save)
b2.grid(column=1, row=4, columnspan=2)

b3 = Button(text="Search", width=14, command=search)
b3.grid(column=2, row=1)

window.mainloop()
