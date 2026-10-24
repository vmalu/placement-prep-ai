# Day 6 - Missing Number

def find_missing_number_sum(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_xor(nums: list[int]) -> int:
    n = len(nums)
    xor_all = 0
    
    # XOR all numbers from 0 to n
    for i in range(n + 1):
        xor_all ^= i
        
    # XOR all elements in the array
    for num in nums:
        xor_all ^= num
        
    return xor_all

# Test cases
test1 = [3, 0, 1]
test2 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
test3 = [0, 1]

print("Test 1 (Sum):", find_missing_number_sum(test1))  # Expected: 2
print("Test 1 (XOR):", find_missing_number_xor(test1))  # Expected: 2

print("Test 2 (Sum):", find_missing_number_sum(test2))  # Expected: 8
print("Test 2 (XOR):", find_missing_number_xor(test2))  # Expected: 8

print("Test 3 (Sum):", find_missing_number_sum(test3))  # Expected: 2
