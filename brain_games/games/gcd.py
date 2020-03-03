from random import randint
from math import gcd


def main():
    first_number, second_number = randint(1, 99), randint(1, 99)
    if gcd(first_number, second_number) == 1:
        while gcd(first_number, second_number) == 1:
            first_number, second_number = randint(1, 99), randint(1, 99)
    question = first_number, second_number
    answer = gcd(first_number, second_number)
    return question, answer
