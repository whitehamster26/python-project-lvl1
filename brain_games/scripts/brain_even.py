from .. import cli
from ..apps import even


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = cli.welcome_user()
    even.main(name)


if __name__ == '__main__':
    main()
