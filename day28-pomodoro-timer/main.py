from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
circle_to_do= 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global circle_to_do
    circle_to_do = 0
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    Time_title.config(text="Timer",fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global circle_to_do
    circle_to_do +=1
    
    working_sec = WORK_MIN*60
    short_sec = SHORT_BREAK_MIN *60
    long_sec = LONG_BREAK_MIN*60
    # do-short-do-short-do-short-do-long
    # 1st-2ed-3rd-4th-5th-8th-9th-10th    
    
    if circle_to_do % 8 == 0:
        Time_title.config(text="Break",fg=GREEN)
        count_down(long_sec)
    elif circle_to_do % 2 ==0:
        Time_title.config(text="Short-Break",fg=PINK)
        count_down(short_sec)
    else:
        Time_title.config(text="Work",fg=RED)
        count_down(working_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count/60)
    second = math.floor(count % 60)
    if second < 10:
        second = f"0{second}"
        
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text,text=f"{minutes}:{second}")
    if count > 0:
        global timer  # 因為如果要cancel 掉tkinter 的 after 需要變成變數
        timer  = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark= ""
        work_sessions = math.floor(circle_to_do/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

#Label
Time_title = Label(text="Timer",fg=GREEN,bg=YELLOW, font=("Curier", 40, "bold"))
Time_title.grid(column=1, row=0)


#Canvas widget
canvas =Canvas(width = 200, height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="day28-pomodoro-timer/tomato.png")  # to find the file
canvas.create_image(100,110, image=tomato_image)   # (x, y , image=)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1 ,row=2)


#button
start_button = Button(text="start",command=start_timer)
start_button.grid(column=0, row=3)



reset_button = Button(text="reset",command = reset_timer)
reset_button.grid(column=2, row=3)

#check_label
check_label = Label(fg=GREEN,bg=YELLOW, font=(FONT_NAME, 12, 'bold'))
check_label.grid(column=1, row=4)




window.mainloop()