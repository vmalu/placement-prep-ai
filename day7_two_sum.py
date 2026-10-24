# Day 7 - Two Sum (Hash Map)

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # Stores {number: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
            
        seen[num] = i
        
    return []

# Test cases
print("Test 1:", two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print("Test 2:", two_sum([3, 2, 4], 6))       # Expected: [1, 2]
print("Test 3:", two_sum([3, 3], 6))          # Expected: [0, 1]
