# Day 11- Reverse a Singly Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next  # Step 1: Save next node
        curr.next = prev       # Step 2: Reverse pointer
        prev = curr            # Step 3: Advance prev
        curr = next_node       # Step 4: Advance curr
        
    return prev  # New head of reversed list

# Helper functions to build and print lists
def build_linked_list(values: list[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_linked_list(head: ListNode) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# Test cases
# Test 1: 1 -> 2 -> 3 -> 4 -> 5
list1 = build_linked_list([1, 2, 3, 4, 5])
reversed1 = reverse_linked_list(list1)
print("Reversed List 1:", print_linked_list(reversed1))  # Expected: [5, 4, 3, 2, 1]

# Test 2: 10 -> 20
list2 = build_linked_list([10, 20])
reversed2 = reverse_linked_list(list2)
print("Reversed List 2:", print_linked_list(reversed2))  # Expected: [20, 10]
