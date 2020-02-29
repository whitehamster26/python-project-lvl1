from ..games import calc
from ..apps import source


def main():
    description = 'What is the result of the expression?'
    source.main(calc, description)


if __name__ == '__main__':
    main()
