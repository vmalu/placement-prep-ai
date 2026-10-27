# Day 10 - Detect Cycle in Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    if head is None or head.next is None:
        return False
        
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        # If pointers meet, a cycle exists
        if slow == fast:
            return True
            
    return False

# Test Case 1: List with a cycle (1 -> 2 -> 3 -> 4 -> points back to 2)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates loop back to node2

print("Test 1 (Has Cycle):", has_cycle(node1))  # Expected: True

# Test Case 2: Linear list without a cycle (10 -> 20 -> 30 -> None)
linear_head = ListNode(10, ListNode(20, ListNode(30)))
print("Test 2 (No Cycle):", has_cycle(linear_head))  # Expected: False
