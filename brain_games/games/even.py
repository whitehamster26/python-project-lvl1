from random import randint


def main():
    number = randint(1, 99)
    correct_answer = number % 2 == 0
    return number, correct_answer
