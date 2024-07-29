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
        prime = [True for _ in range(max_n + 1)]
        p = 2
        while (p * p <= max_n):
            if prime[p] is True:
                for i in range(p * p, max_n + 1, p):
                    prime[i] = False
            p += 1
        return [p for p in range(2, max_n + 1) if prime[p]]

    def playGame(n):
        if n == 1:
            return "Ben"
        primes = sieveOfEratosthenes(n)
        remaining = set(range(1, n + 1))
        turn = 0
        while primes:
            curPrime = primes.pop(0)
            for multiple in range(curPrime, n + 1, curPrime):
                if multiple in remaining:
                    remaining.remove(multiple)
            primes = [p for p in primes if p in remaining]
            turn = 1 - turn
        return "Ben" if turn == 0 else "Maria"


    if x <= 0 or not nums:
        return None

    mariaWins = 0
    benWins = 0

    for n in nums:
        winner = playGame(n)
        if winner == "Maria":
            mariaWins += 1
        else:
            benWins +=1

    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
