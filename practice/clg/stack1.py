class stacks:
    def __init_(self):
        self.stack = []
        self.Top = -1

    def isempty(self):
        if(self.Top == -1):
            return True
        else:
            return False
            


    def push(self, Value):
        self.Top = self.Top + 1
        self.stack[self.Top] = Value

    def pop(self):
        self.Top = self.Top - 1

    def peek(self):
        return self.stack[self.Top]

    def see(self):
        for i in self.stack

s = stacks 
s.push(10)
s.push(20)
s.push(30)

print(s.peek())