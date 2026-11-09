# Day 20 - Climbing Stairs (Python 3)

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
        
    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2
    
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
        
    return prev1

# Test cases
print("Ways to climb 2 stairs:", climb_stairs(2))  # Expected: 2 (1+1, 2)
print("Ways to climb 3 stairs:", climb_stairs(3))  # Expected: 3 (1+1+1, 1+2, 2+1)
print("Ways to climb 5 stairs:", climb_stairs(5))  # Expected: 8
