# Day 22 - Coin Change (Python 3)

def min_coins_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
                
    return dp[amount] if dp[amount] != float('inf') else -1

# Test cases
print("Coins [1, 2, 5], Amount 11:", min_coins_change([1, 2, 5], 11))  # Expected: 3 (5 + 5 + 1)
print("Coins [2], Amount 3:", min_coins_change([2], 3))                # Expected: -1 (Impossible)
print("Coins [1, 6, 9], Amount 12:", min_coins_change([1, 6, 9], 12))  # Expected: 2 (6 + 6)
