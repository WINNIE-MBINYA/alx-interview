#!/usr/bin/python3
def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount"""
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make 0

    # Update the dp array with the minimum coins needed for each amount
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we couldn't make the amount
    if dp[total] == float('inf'):
        return -1
    return dp[total]


# Main file for testing
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
