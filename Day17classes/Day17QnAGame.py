from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    new_question = Question(data['question'], data['correct_answer'])
    # important to make a variable in order for the loop to make the object unique, or else Question() object with no values will just be added
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
