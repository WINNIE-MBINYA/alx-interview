#!/usr/bin/python3
"""
This module contains the makeChange function that determines the fewest
number of coins needed to meet a given amount.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of integers representing the values of coins.
        total (int): The amount to achieve using the fewest coins possible.
        
    Returns:
        int: The fewest number of coins needed to meet total.
             If the total is 0 or less, returns 0.
             If the total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                # Early exit if we find a solution for the total
                if dp[total] != float('inf'):
                    return dp[total]

    return dp[total] if dp[total] != float('inf') else -1
