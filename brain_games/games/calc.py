from random import randint


def main():
    operators = {1: '+', 2: '-', 3: '*'}
    first_number, second_number = randint(1, 99), randint(1, 99)
    operator = randint(1, 3)
    if operator == 1:
        answer = first_number + second_number
    elif operator == 2:
        answer = first_number - second_number
    elif operator == 3:
        second_number = randint(1, 12)
        answer = first_number * second_number
    question = f'{first_number} {operators[operator]} {second_number}'
    return question, answer
