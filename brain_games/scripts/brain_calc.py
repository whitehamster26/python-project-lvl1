from .. import cli
from ..games import calc
from ..apps import source


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    name = cli.welcome_user()
    source.main(name, calc)


if __name__ == '__main__':
    main()
