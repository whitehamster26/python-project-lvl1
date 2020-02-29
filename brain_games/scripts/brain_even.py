from .. import cli
from ..games import even
from ..apps import source


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = cli.welcome_user()
    source.main(name, even)


if __name__ == '__main__':
    main()
