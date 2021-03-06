from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(first_number, second_number):
    while second_number:
        first_number, second_number = second_number, \
            first_number % second_number
    return first_number


def start():
    first_number = randint(1, 99)
    second_number = randint(1, 99)
    question = f'{first_number} {second_number}'
    answer = gcd(first_number, second_number)
    return question, str(answer)
