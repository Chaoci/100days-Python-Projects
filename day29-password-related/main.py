from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle
FONT = ("Curier", 10, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for x in range(randint(8, 10))]
    password_list1=[choice(symbols) for x in range(randint(2, 4))]
    password_list2=[choice(numbers) for x in range(randint(2, 4))]

    password_final = password_list+ password_list1+password_list2

    shuffle(password_final)

    password_g = "".join(password_final)

    password_input.insert(0,password_g)
    pyperclip.copy(password_g)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    web = web_input.get()
    mail= email_input.get()
    password = password_input.get()
    
    #message box
    if len(web) == 0 or len(mail) ==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please Don't leave any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:\nEmail: {mail} \nPassword:{password} \nIs it ok to save?")
    
    if is_ok:
        with open("day29-password-related/data.txt","a") as file:
            file.write(f"{web} | {mail} | {password} \n")
            clear()
        
def clear():
    web_input.delete(0,END)
    password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password-manager")
window.config(padx=20, pady=20,bg="white")


#canvas widget
canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
locker_image = PhotoImage(file="day29-password-related\logo.png")
canvas.create_image(100,100,image=locker_image)
canvas.grid(column=1,row=0)

#Label
website_label = Label(text="Website:",bg="white", font=FONT)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:",bg="white",font=FONT)
email_label.grid(column=0, row=2)
password_label = Label(text="Password",bg="white",font=FONT)
password_label.grid(column=0,row=3)

#Enter
web_input = Entry(width=38)
web_input.grid(column=1,row=1,columnspan=2)

#focus
web_input.focus()
email_input = Entry(width=38)
email_input.grid(column=1, row=2,columnspan=2)

#insert
email_input.insert(0, "a20264520@gmail.com")

password_input = Entry(width=22)
password_input.grid(column=1, row=3)

#button

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=38,command=get_data)
add_button.grid(column=1,columnspan=2, row=4)
window.mainloop()