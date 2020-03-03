from random import randint


def main():
    question = randint(1, 100)
    answer = False
    if question > 1:
        if question in (2, 3, 5):
            answer = True
        else:
            for _ in range(2, question // 2):
                if question % _ == 0:
                    answer = False
                    break
                else:
                    answer = True
    return question, answer
