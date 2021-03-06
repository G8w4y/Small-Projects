from re import S
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dic in question_data:
    question = Question(dic["question"], dic["correct_answer"])
    question_bank.append(question)

# print(question_data[0]["text"])

# print(question_bank[0].text)

# print(question_data[1]["text"])

# print(question_bank[1].text)

# print(question_bank)

quiz_brain = QuizBrain(question_bank)
# print(quiz_brain.question_number)

while quiz_brain.still_has_questions(question_bank):
    quiz_brain.next_question()
print(f"You've completed the quiz!\nYour final score was: \
    {quiz_brain.correct_guesses}/{len(question_bank)}")
