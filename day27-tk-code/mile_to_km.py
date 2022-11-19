from tkinter import*

from matplotlib.pyplot import margins

window = Tk()
window.minsize(width=200, height= 100)
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

unit_miles = Label(text="Mile")
unit_km = Label(text="Km")
is_equal_to = Label(text="is equal to")
unit_miles.grid(column=2, row=0)
unit_km.grid(column=2, row=1)
is_equal_to.grid(column=0, row=1)

ans_label= Label(text="0")
ans_label.grid(column=1,row=1)

input_mile = Entry(width= 5)
input_mile.grid(column=1,row=0)

def calculate():
    result = round(int(input_mile.get()) * 1.609, 2)
    ans_label.config(text=f"{result}")

button = Button(text="Calculate",command = calculate)
button.grid(column=1,row=3)










window.mainloop()