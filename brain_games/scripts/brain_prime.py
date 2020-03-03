from ..games import prime
from ..apps import source


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer \
"no".'
    source.main(prime, description)


if __name__ == '__main__':
    main()
