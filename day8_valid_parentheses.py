# Day 8 - Valid Parentheses (Stack)

def is_valid_parentheses(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
        
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return len(stack) == 0

# Test cases
print("Test 1 (Balanced):", is_valid_parentheses("()[]{}"))  # Expected: True
print("Test 2 (Nested):", is_valid_parentheses("{[()]}"))    # Expected: True
print("Test 3 (Mismatched):", is_valid_parentheses("([)]"))  # Expected: False
print("Test 4 (Incomplete):", is_valid_parentheses("(()"))   # Expected: False
print("Test 5 (Leading Close):", is_valid_parentheses("]"))  # Expected: False
