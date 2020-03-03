from ..games import progression
from ..apps import source


def main():
    description = 'What number is missing in the progression?'
    source.main(progression, description)


if __name__ == '__main__':
    main()
