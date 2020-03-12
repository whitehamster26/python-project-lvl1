from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = [('+', add), ('-', sub), ('*', mul)]


def start():
    first_number = randint(1, 99)
    second_number = randint(1, 99)
    operator, operation = choice(OPERATIONS)
    question = f'{first_number} {operator} {second_number}'
    answer = operation(first_number, second_number)
    return question, str(answer)
