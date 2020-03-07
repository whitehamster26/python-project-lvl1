from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def start():
    start = randint(1, 20)
    step = randint(1, 10)
    items = [str(start + item*step) for item in range(9)]
    missed_item = randint(0, len(items))
    answer = items[missed_item]
    items[missed_item] = '..'
    question = ' '.join(items)
    return question, answer
