from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer \
"no".'


def prime_check(number):
    if number < 2:
        result = False
    elif number in (2, 3, 5):
        result = True
    else:
        for i in range(2, number // 2):
            if number % i == 0:
                result = False
                break
            else:
                result = True
    return result


def start():
    question = randint(1, 100)
    answer = 'yes' if prime_check(question) else 'no'
    return question, answer
