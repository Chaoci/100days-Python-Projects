from question_model import Question
from data import question_data, new_data
from quiz_brain import QuizBrian

question_bank = []
for i in new_data:
    question_bank.append(Question(i['question'],i['correct_answer']))

quiz = QuizBrian(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz.")
print(f"Your final score was:{quiz.score}/{quiz.q_num}.")