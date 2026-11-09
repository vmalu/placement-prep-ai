# Day 14 - Queue Using Two Stacks

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._shift_stacks()
        if self.out_stack:
            return self.out_stack.pop()
        return -1

    def peek(self) -> int:
        self._shift_stacks()
        if self.out_stack:
            return self.out_stack[-1]
        return -1

    def is_empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def _shift_stacks(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

# Test cases
q = MyQueue()
q.push(10)
q.push(20)
q.push(30)

print("Front Element (Peek):", q.peek())  # Expected: 10
print("Dequeued Element:", q.pop())        # Expected: 10
print("New Front Element:", q.peek())       # Expected: 20
print("Is Queue Empty?:", q.is_empty())     # Expected: False
