from ..games import even
from ..apps import source


def main():
    description = 'Answer "yes" if number even otherwise answer "no".'
    source.main(even, description)


if __name__ == '__main__':
    main()
