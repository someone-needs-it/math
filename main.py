import random
def generator_math_question(a,b):
    num1 = random.randint(a,b)
    num2 = random.randint(a,b)
    operator = random.choice(["+","-","/","*"])
    return f"{num1} {operator} {num2}"
def check_answer(quenstion,user_answer):
    try:
        user_answer = float(user_answer)
        if "/" in quenstion:
            return round(user_answer, 1) == eval(quenstion)
        return user_answer == eval(quenstion)
    except ValueError:
        return False
def math_quiz(number_of_questions=5):
    print("Добро пожаловать на математический тест")
    correct_answers = 0
    for i in range(number_of_questions):
        question = generator_math_question(1,10)
        answer_player = input(f"{question} = ")
        if check_answer(question, answer_player):
            correct_answers += 1
    print("Тест завершен")
    print(f"Правильных ответов = {correct_answers} из {number_of_questions}")
    if correct_answers >= number_of_questions * 0.8:
        print("Оценка А")
    elif correct_answers >= number_of_questions * 0.6:
        print("Оценка B")
    else:
        print("Оценка С")
math_quiz(5)





























