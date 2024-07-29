#!/usr/bin/python3
""" isWinner Module """


def counting(num):
    """ num [int]: integer
        Returns: Composite numbers
    """
    return [i for i in range(2, num + 1)]


def is_prime(n):
    """ checks the prime of integers
        Paramters:
            n [int]: integer
        Returns: boolean
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ It iterates through an array of integers and picks
        prime numbers

    Parameters:
        x [int]: number of rounds to be played
        nums [list]: array of integers

    Returns: player with most win
    """
    x_count, y_count = 0, 0
    x_turn = True

    for _ in range(x):
        for i in nums:
            arr = counting(i)
            while arr:
                for num in arr:
                    if is_prime(num):
                        prime = num
                        break
                else:
                    break

                if x_turn:
                    x_count += 1
                else:
                    y_count += 1

                arr = [n for n in arr if n % prime != 0]

                x_turn = not x_turn

    if x_count > y_count:
        return "Maria"
    else:
        return "Ben"
