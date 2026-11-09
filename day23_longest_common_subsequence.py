# Day 23 - Longest Common Subsequence (Python 3)

def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    # Create (m + 1) x (n + 1) DP table initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    return dp[m][n]

# Test cases
print("LCS of ('abcde', 'ace'):", longest_common_subsequence("abcde", "ace"))  # Expected: 3 ('ace')
print("LCS of ('abc', 'abc'):", longest_common_subsequence("abc", "abc"))      # Expected: 3
print("LCS of ('abc', 'def'):", longest_common_subsequence("abc", "def"))      # Expected: 0
