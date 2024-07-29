#!/usr/bin/python3
""" isWinner Module """


def isWinner(x, nums):
    """ It iterates through an array of integers and picks
        prime numbers

    Parameters:
        x [int]: number of rounds to be played
        nums [list]: array of integers

    Returns: player with most win
    """
    def sieveOfEratosthenes(max_n):
        """ create a boolean array 'prime[0:max_n]' and initialize all
            entries as true

            prime[i] will be false if not a prime or else true
        """
        prime = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if prime[p]:
                for i in range(p * p, max_n + 1, p):
                    prime[i] = False
            p += 1
        return [p for p in range(2, max_n + 1) if prime[p]]

    def playGame(n, primes):
        if n == 1:
            return "Ben"
        remaining = set(range(1, n + 1))
        turn = 0
        while True:
            avail_prime = None
            for prime in primes:
                if prime in remaining:
                    avail_prime = prime
                    break
            if avail_prime is None:
                break
            for multiple in range(avail_prime, n + 1, avail_prime):
                remaining.discard(multiple)
            turn = 1 - turn
        return "Ben" if turn == 0 else "Maria"

    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieveOfEratosthenes(max_n)

    mariaWins = 0
    benWins = 0

    for n in nums:
        winner = playGame(n, primes)
        if winner == "Maria":
            mariaWins += 1
        else:
            benWins += 1

    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
