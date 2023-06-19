from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open(file="data.json", mode="r") as df:
            web_dict = json.load(df)
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title="Error", message="Sorry you haven't saved anything")
    else:
        website = web_entry.get()
        if website in web_dict:
            messagebox.showinfo(title=website,
                                message=f"Email : {web_dict[website]['email']}\n"
                                        f"Password : {web_dict[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"Sorry you haven't saved any records for {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        df = open("data.json", mode="r")
        webdict = json.load(df)
    except FileNotFoundError and json.decoder.JSONDecodeError:
        webdict = {}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    elif website in webdict:
        ans = messagebox.askokcancel(title="Record exists", message="Do you want to update the records of this website")
        if ans:
            is_ok = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered:\nEmail: {email} \n"
                                                   f"Password: {password}\nIs it ok to save")
            if is_ok:
                try:
                    with open("data.json", mode="r") as dataf:
                        # read data
                        data = json.load(dataf)

                except FileNotFoundError and json.decoder.JSONDecodeError:
                    with open("data.json", mode="w") as dataf:
                        # write
                        json.dump(new_data, dataf, indent=4)
                else:
                    # update
                    data.update(new_data)
                    with open("data.json", mode="w") as dataf:
                        # write
                        json.dump(data, dataf, indent=4)
                finally:
                    web_entry.delete(0, END)
                    pass_entry.delete(0, END)
                    web_entry.focus()
            df.close()

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:"
                                               f"\nEmail: {email} \n"
                                               f"Password: {password}\nIs it ok to save")
        if is_ok:
            try:
                with open("data.json", mode="r") as dataf:
                    # read data
                    data = json.load(dataf)

            except FileNotFoundError and json.decoder.JSONDecodeError:
                with open("data.json", mode="w") as dataf:
                    # write
                    json.dump(new_data, dataf, indent=4)
            else:
                # update
                data.update(new_data)
                with open("data.json", mode="w") as dataf:
                    # write
                    json.dump(data, dataf, indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
                web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

Email_label = Label(text="Email/Username:")
Email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# entry
web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=1)

email_entry = Entry(width=39)
email_entry.insert(0, "shahharshil686@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

gen_button = Button(text="Generate Password", command=gen_pass)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
