from random import randint


def main(name):
    answers = {'yes': 1, 'no': 0}
    answers_result = {True: 'yes', False: 'no'}
    correct_answers = 0
    user_answer = None
    correct_answer = False
    while correct_answers < 3:
        number = randint(1, 99)
        correct_answer = number % 2 == 0
        while user_answer not in answers:
            user_answer = input(f'Question: {number} ')
        if answers[user_answer] == correct_answer:
            correct_answers += 1
        else:
            break
        user_answer = None
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was \
'{answers_result[correct_answer]}'.")


if __name__ == "__main__":
    main()
