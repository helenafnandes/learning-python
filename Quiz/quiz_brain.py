class QuizBrain:

    def __init__(self, question_bank):
        self.questions_list = question_bank
        self.current_question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.current_question_number]
        user_answer = input(f"Q.{self.current_question_number + 1}: {current_question.text} (True/False): ")
        self.current_question_number += 1
        self.check_answer(user_answer, current_question.answer)
        print("\n")

    def still_has_questions(self):
        # if self.current_question_number < len(self.questions_list):
        #     return True
        # else:
        #     return False
        return self.current_question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():  # True, true, TRUE
            print("Correct!")
            self.score += 1
        else:
            print("Wrong...")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.current_question_number}")
    # def ask_question(self):
    #
    # def check_answer(self):
    #
    # def check_end(self):