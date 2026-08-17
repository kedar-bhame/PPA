class Stack:
    def __init__(self):
        self.size = 10
        self.stack = [0] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack overflow")
            return

        self.top = self.top + 1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return None

        value = self.stack[self.top]
        self.top = self.top - 1
        return value

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        return self.stack[self.top]

    def display(self):
        if self.top == -1:
            print("Stack is empty")
            return

        index = self.top
        while index >= 0:
            print(self.stack[index])
            index = index - 1


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack elements:")
    stack.display()
    print("Popped:", stack.pop())
    print("Top:", stack.peek())
