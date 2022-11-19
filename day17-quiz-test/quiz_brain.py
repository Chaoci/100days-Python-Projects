# https://opentdb.com/ 可以更換data資料 來問問題 產生api
class QuizBrian: 
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list 
        self.score = 0
        
    def still_has_question(self):
        return self.q_num < len(self.q_list)
        
        
    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        ans = input(f"Q.{self.q_num}: {current_question.question} (True/False) :")
        self.check_answer(ans, current_question.answer)
        
    def check_answer(self, ans, correct_answer):
        if ans.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score {self.score}/{self.q_num}.")
        print("\n")
        

