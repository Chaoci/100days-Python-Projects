from tkinter import*
from tkinter import messagebox
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card ={}
data = {}
#-------------------------------- GET DATA ---------------------------------#
try:
    data = pd.read_csv("day31-flashcard/flash-card-project-start/data/learned.csv")
except FileNotFoundError:   
    origin_data = pd.read_csv("day31-flashcard/flash-card-project-start/data/vocabulary1.csv")
    origin_data.to_dict(orient="record")
else:
    data  = data.to_dict(orient="record")  # orient="record" {"a":"b"}的方式呈現

#------------------------------- SET FUNCTION ------------------------------#
# def wrong_button():
#     canvas.create_image(410,276,image=back_card)
#     pass

def correct_button():
    global current_card, flip_timer #取消掉他只要三秒就一定會跳掉的狀態
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(old,image=front_card)
    canvas.itemconfig(vocabulary,text=f"{current_card['english']}",fill="black")
    canvas.itemconfig(language,text="English",fill="black")
    flip_timer = window.after(3000,change_back_card)


def is_known():
    global data
    data.remove(current_card)
    new_data = pd.DataFrame(data)
    new_data.to_csv("day31-flashcard/flash-card-project-start/data/learned.csv",index=False)
    correct_button()
    
def change_back_card():
    global current_card
    canvas.itemconfig(old,image=back_card)
    canvas.itemconfig(vocabulary,text=f"{current_card['中文']}",fill="white")
    canvas.itemconfig(language,text="中文",fill="white")
    

#------------------------------- UI APPEARANCE -----------------------------#

window = Tk()
window.title("Vocabulary memorise")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# image
front_card = PhotoImage(file ="day31-flashcard/flash-card-project-start/images/card_front.png")
back_card = PhotoImage(file ="day31-flashcard/flash-card-project-start/images/card_back.png")
correct = PhotoImage(file ="day31-flashcard/flash-card-project-start/images/right.png")
wrong = PhotoImage(file="day31-flashcard/flash-card-project-start/images/wrong.png")

#canvas
canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)

old = canvas.create_image(410, 276,image = front_card)
canvas.grid(column=1, row=0, columnspan=3)

# canvas.create_image(410,276,image=back_card)

#Label
language = canvas.create_text(400,150,text="", fill="black", font=("Ariel",40,"italic"))
vocabulary = canvas.create_text(400,263, text="",fill="black",font=("Ariel",60,"bold"))

#Button
wrong_button = Button(image=wrong,highlightthickness=0, bg=BACKGROUND_COLOR,borderwidth=0,command=correct_button)
wrong_button.grid(column=1, row=4)

right_button = Button(image=correct, highlightthickness=0, bg=BACKGROUND_COLOR,borderwidth=0, command=is_known)
right_button.grid(column=3, row=4)


flip_timer = window.after(3000,change_back_card)
correct_button()




window.mainloop()
