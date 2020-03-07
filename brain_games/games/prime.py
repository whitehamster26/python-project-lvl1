from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer \
"no".'


def prime_check(number):
    result = False  # in case if number = 0 or 1
    if number > 1:
        if number in (2, 3, 5):
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
