#!/usr/bin/env python3


def hotel(n: str) -> dict:
    '''Return the amount of numbers signs that needed to be made to use them for hotel rooms.'''
    try:
        n = int(n)

        signs_amount = {}
        for digit in range(10):
            signs_amount[str(digit)] = 0

        for number in range(1, n + 1):
            for symbol in str(number):
                signs_amount[symbol] += 1

        return signs_amount

    except ValueError:
        print('Enter any natural number greater than 0!')
        n = input('> ')
        return hotel(n)


def start():
    print('\nHow many rooms in your hotel?\n')
    n = input('> ')
    result = hotel(n)

    print()
    for key, val in result.items():
        print(key, '->', val)
    print()


if __name__ == '__main__':
    start()

