from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip
import json

FONT_NAME = "Courier"

# ----------------------------- SEARCH OPTION ----------------------------- #


def search():
    remember_web = str(website_box.get().title())
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Not Exists", message="The DB File not Exists")
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(title="Not Exists", message="The DB File is Empty")
    else:
        if remember_web in data:
            add_button.config(text="Update")
            email_username_box.delete(0, END)
            password_box.delete(0, END)
            email_username_box.insert(0, data[remember_web]["Email"])
            password_box.insert(0, data[remember_web]["Password"])
            messagebox.showinfo(title="Exists", message="This Site is Exists")
        else:
            if remember_web == "":
                messagebox.showwarning(title="Not Exists", message="You Insert Nothing")
            else:
                messagebox.showwarning(title="Not Exists", message=f"This '{remember_web}' Site is not Exists")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def set_password():
    password_box.delete(0, END)
    password = Password()
    password_box.insert(0, password.password)
    pyperclip.copy(password.password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = website_box.get().title()
    email = email_username_box.get()
    password = password_box.get()
    new_data = {
        web: {
            "Email": email,
            "Password": password,
        }
    }

    if len(password) == 0 or len(web) == 0 or len(email) == 0:
        messagebox.showwarning(title="Warning", message="Please fill in all the requested values")

    else:
        is_ok = messagebox.askokcancel(title="Password Save", message=f"Are you sure?\nEmail:{email}"
                                                                      f"\nPassword {password}")

        try:
            with open("data.json", "r") as file:
                # Read File.json
                data = json.load(file)
                # Update File.json
                data.update(new_data)
            with open("data.json", "w") as file:
                # Write on File.json
                json.dump(data, file, indent=3)
        except FileNotFoundError:
            # When file.json doesn't exists
            with open("data.json", "w") as file:
                # Write on File.json
                json.dump(new_data, file, indent=3)
        except json.decoder.JSONDecodeError:
            # When File exists But is empty
            with open("data.json", "w") as file:
                # Write on File.json
                json.dump(new_data, file, indent=3)
        if is_ok:

            # file.write(f"{web} | {email} | {password}\n")
            website_box.delete(0, END)
            email_username_box.delete(0, END)
            password_box.delete(0, END)
            # برای نمایش یک پاپ آپ که مثلا بعد از زدن دکمه ی ادد ، بگه پسورد ذخیره شد
            messagebox.showinfo(title="Save Password", message="Your Password Save Successfully")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# این میاد از بالا و پایین - چپ و راست ، به اندازه عددی که وارد میکنیم ، فضا خالی میکنه ، انگار مرز درست میکنه
window.config(padx=25, pady=20, bg="#f7f5dd")
# این اندازه ی صفحه ای که نمایش داده میشه رو نشون میده ، اگه پدایکس و پدایگرگ نزاشته باشیم ، اندازه ی خالص میشه چون دیگه مرزی نداره ، رنگ رو عوض کنیم
canvas = Canvas(width=200, height=200, bg="#f7f5dd", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
# این میاد میگه عکس توی چه پوزیشنی از صفحه ی کانواس وایسه ، ربطی به اندازه ی عکس نداره ،
canvas.create_image(90, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="#f7f5dd", font=FONT_NAME)
website_label.grid(column=0, row=1)

website_box = Entry(width=40, bg="#e2979c")
website_box.focus()
website_box.grid(column=1, row=1, columnspan=2)
# website_box.insert(0, "Facebook")

email_username_label = Label(text="Email/Username:", bg="#f7f5dd", font=FONT_NAME)
email_username_label.grid(column=0, row=2)

email_username_box = Entry(width=40, bg="#e2979c")
email_username_box.focus()
email_username_box.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", bg="#f7f5dd", font=FONT_NAME)
password_label.grid(column=0, row=3)

password_box = Entry(width=31, bg="#e2979c")
password_box.focus()
password_box.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=set_password, bg="#dcaf94")
generate_password.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=7, command=search, bg="#dcaf94")
search_button.grid(row=1, column=3, columnspan=2)


window.mainloop()
