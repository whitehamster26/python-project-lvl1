from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def start():
    question = randint(1, 99)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
