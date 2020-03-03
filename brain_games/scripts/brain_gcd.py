from ..games import gcd
from ..apps import source


def main():
    description = 'Find the greatest common divisor of given numbers.'
    source.main(gcd, description)


if __name__ == '__main__':
    main()
