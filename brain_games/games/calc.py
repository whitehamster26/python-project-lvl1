from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def start():
    operations = [('+', add), ('-', sub), ('*', mul)]
    first_number = randint(1, 99)
    second_number = randint(1, 99)
    operator, operation = choice(operations)
    question = f'{first_number} {operator} {second_number}'
    answer = operation(first_number, second_number)
    return question, str(answer)
