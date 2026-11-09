# Day 21 - Kadane's Algorithm (Python 3)

def max_subarray_sum(nums: list[int]) -> int:
    if not nums:
        return 0
        
    current_sum = nums[0]
    max_so_far = nums[0]
    
    for i in range(1, len(nums)):
        # Extend existing subarray or start a new subarray
        current_sum = max(nums[i], current_sum + nums[i])
        max_so_far = max(max_so_far, current_sum)
        
    return max_so_far

# Test cases
test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test2 = [1]
test3 = [5, 4, -1, 7, 8]
test4 = [-5, -2, -8, -1]  # All negative numbers

print("Test 1 Max Subarray Sum:", max_subarray_sum(test1))  # Expected: 6 (subarray [4, -1, 2, 1])
print("Test 2 Max Subarray Sum:", max_subarray_sum(test2))  # Expected: 1
print("Test 3 Max Subarray Sum:", max_subarray_sum(test3))  # Expected: 23
print("Test 4 Max Subarray Sum:", max_subarray_sum(test4))  # Expected: -1
