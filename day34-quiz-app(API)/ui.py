from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain  #為了拿另外一個class的function
        self.ans_t = "True"
        self.ans_f = "False"
        self.quiz.score = 0
        
        self.window = Tk()
        self.window.title("QuizApp")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        #label
        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",14,"normal"))
        self.score_label.grid(row=0,column=1)
        
        #canvas
        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,     # 內容自動換行
            text="questions here",
            fill=THEME_COLOR, 
            font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50) 

        #button
        correct_b = PhotoImage(file="images/true.png")
        wrong_b = PhotoImage(file="images/false.png")
        self.true_button = Button(image=correct_b,border=0,highlightthickness=0,command=self.True_answer)
        self.true_button.grid(column=0, row=3)
        self.false_button = Button(image=wrong_b,border=0,highlightthickness=0,command=self.False_answer)
        self.false_button.grid(column=1,row=3)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question() 
            self.score_label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"Your Final Score {self.quiz.score}!")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")
        
    def True_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def False_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        