from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height= 300)
window.config(padx=20, pady=20)  # padding like css

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)

# my_label["text"] = "new text"
# my_label.config(text="nwe text")   change value of label
def button_clicked():  
    my_label.config(text=input.get())
    

button = Button(text="click me",command = button_clicked)
button2 = Button(text=" New button")
button.grid(column=1, row=1)
button2.grid(column=2, row=0)

#Entry

input = Entry(width = 10)
input.grid(column=3, row=2)
#input.get() can get the word from input




window.mainloop()