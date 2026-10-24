# Day 5 - Valid Anagram Check

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    counts = {}
    
    # Step 1: Count characters in first string
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    # Step 2: Decrement counts with second string
    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1
        
    return True

# Test cases
print("Test 1 (listen, silent):", is_anagram("listen", "silent"))    # Expected: True
print("Test 2 (triangle, integral):", is_anagram("triangle", "integral"))  # Expected: True
print("Test 3 (rat, car):", is_anagram("rat", "car"))                # Expected: False
print("Test 4 (aab, abb):", is_anagram("aab", "abb"))                # Expected: False
