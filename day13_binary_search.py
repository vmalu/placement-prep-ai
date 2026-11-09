# Day 13 - Iterative Binary Search

def binary_search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        # Prevents integer overflow
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

# Test cases
sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print("Test 1 (Found at index 5):", binary_search(sorted_arr, 23))  # Expected: 5
print("Test 2 (Found at index 0):", binary_search(sorted_arr, 2))   # Expected: 0
print("Test 3 (Not Found):", binary_search(sorted_arr, 50))         # Expected: -1
