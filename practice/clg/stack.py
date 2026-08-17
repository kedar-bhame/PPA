class Stack:
    """A simple fixed-capacity stack."""

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            return
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def display(self):
        print(self.items[::-1])  # top item appears first


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Popped:", stack.pop())
    print("Top:", stack.peek())
