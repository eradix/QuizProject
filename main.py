from Question import Question
from data import QuizData, get_user_inputs
from QuestionBrain import QuestionBrain
from logo import logo


if __name__ == '__main__':

    print(logo)

    user_inputs = get_user_inputs()

    quiz_data = QuizData(user_inputs['amount'], user_inputs['category'])

    question_data = quiz_data.create_quiz_data()

    print("START OF QUIZ")

    questions = []
    for q in question_data:
        questions.append(Question(q['question'], q['correct_answer'], q['category']))

    quiz = QuestionBrain(questions)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You completed the quiz.")
    print(f"Your final score is {quiz.score}/{len(quiz.question_list)}.")
