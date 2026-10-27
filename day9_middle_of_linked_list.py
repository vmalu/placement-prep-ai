# Day 9 - Middle of a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle_node(head: ListNode) -> ListNode:
    slow = head
    fast = head
    
    # Fast moves 2 steps while slow moves 1 step
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    return slow

# Helper function to create linked list from list
def build_linked_list(values: list[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

# Test cases
# Test 1 (Odd length: 1 -> 2 -> 3 -> 4 -> 5)
odd_list = build_linked_list([1, 2, 3, 4, 5])
middle_odd = find_middle_node(odd_list)
print("Odd List Middle Node:", middle_odd.val)  # Expected: 3

# Test 2 (Even length: 1 -> 2 -> 3 -> 4 -> 5 -> 6)
even_list = build_linked_list([1, 2, 3, 4, 5, 6])
middle_even = find_middle_node(even_list)
print("Even List Middle Node:", middle_even.val)  # Expected: 4
