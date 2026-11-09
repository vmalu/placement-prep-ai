# Day 12 - Merge Two Sorted Linked Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    tail = dummy
    
    # Traverse while both lists have remaining nodes
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    # Splice remaining nodes from whichever list is left
    tail.next = list1 if list1 is not None else list2
    
    return dummy.next

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

# Test case: Merge [1, 2, 4] and [1, 3, 4]
l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])
merged = merge_two_lists(l1, l2)
print("Merged Sorted List:", print_linked_list(merged))  # Expected: [1, 1, 2, 3, 4, 4]
