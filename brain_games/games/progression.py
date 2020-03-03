from random import randint


def main():
    def make_progression(items, step):
        missed_item = randint(1, len(items))
        for index, item in enumerate(items):
            if index == missed_item:
                answer = items[index] * step
                items[index] = ".."
                pass
            else:
                items[index] *= step
                items[index] = str(items[index])
        return ' '.join(items), answer
    step = randint(1, 10)
    items = [item+1 for item in range(10)]
    question, answer = make_progression(items, step)
    return question, answer


if __name__ == "__main__":
    main()
