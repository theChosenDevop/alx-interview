#!/usr/bin/python3
""" 0-making_change module """


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
        coins [list]: A List of Integers representing denomination of
                      coins available
        totals [int]: The amount of money for which we need to
                      make change

    Returns:
        int: Zero if total is empty, total number of coins neede for change
             or -1 if not possible to change further
    """
    tCoin = total
    coins.sort(reverse=True)
    count = 0
    cLen = len(coins)
    if tCoin <= 0:
        return 0
    for index in range(cLen):
        curCoinval = coins[index]
        while tCoin >= curCoinval:
            tCoin = tCoin - curCoinval
            count = count + 1
        if tCoin == 0:
            return count
    else:
        return -1
