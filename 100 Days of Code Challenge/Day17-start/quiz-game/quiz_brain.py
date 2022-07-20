class QuizBrain():
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.correct_guesses = 0

    def still_has_questions(self, q_bank):
        total_questions = len(q_bank)
        return self.question_number < total_questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)
        print(f"The answer was: {current_question.answer}")
        print(f"Score: {self.correct_guesses}/{self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.correct_guesses += 1
