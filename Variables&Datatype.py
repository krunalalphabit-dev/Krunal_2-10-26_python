import tkinter as tk

def register():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if name == "":
        message.config(text="Enter Full Name", fg="red")

    elif "@" not in email or "." not in email:
        message.config(text="Enter Valid Email", fg="red")

    elif not age.isdigit():
        message.config(text="Enter Valid Age", fg="red")

    elif int(age) < 18 or int(age) > 30:
        message.config(text="Age must be 18 to 30", fg="red")

    else:
        message.config(text="Registration Successful!", fg="green")


# Window
w = tk.Tk()
w.title("Student Registration")
w.geometry("400x300")

# Name
tk.Label(w, text="Full Name").pack()
name_entry = tk.Entry(w)
name_entry.pack()

# Email
tk.Label(w, text="Email Address").pack()
email_entry = tk.Entry(w)
email_entry.pack()

# Age
tk.Label(w, text="Age").pack()
age_entry = tk.Entry(w)
age_entry.pack()

# Button
tk.Button(w, text="Register", command=register).pack(pady=10)

# Message
message = tk.Label(w, text="")
message.pack()

w.mainloop()