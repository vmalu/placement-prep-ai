# Day 1: Palindrome Check

def check_palindrome(text: str):
    # Convert to lowercase so 'Madam' and 'madam' are treated equally
    cleaned_text = text.lower()
    
    # Reverse using slicing
    reversed_text = cleaned_text[::-1]
    
    if cleaned_text == reversed_text:
        print(f"'{text}' is a Palindrome!")
    else:
        print(f"'{text}' is NOT a Palindrome.")

# Test inputs
check_palindrome("radar")
check_palindrome("wipro")
check_palindrome("Madam")
