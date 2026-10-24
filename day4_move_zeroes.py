# Day 4 - Move Zeroes to End
def move_zeroes(nums: list[int]) -> list[int]:
    insert_pos = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap current non-zero element with the element at insert_pos
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
            
    return nums

# Test cases
test1 = [0, 1, 0, 3, 12]
test2 = [0, 0, 1]
test3 = [4, 5, 6]

print("Test 1:", move_zeroes(test1))  # Expected: [1, 3, 12, 0, 0]
print("Test 2:", move_zeroes(test2))  # Expected: [1, 0, 0]
print("Test 3:", move_zeroes(test3))  # Expected: [4, 5, 6]
