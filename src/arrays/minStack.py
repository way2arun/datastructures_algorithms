"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.stack = []

    def push(self, x: int) -> None:
        self.array.append(x)
        if len(self.stack) == 0 or x <= self.stack[-1]:
            self.stack.append(x)

    def pop(self) -> None:
        val = self.array.pop()
        if val == self.stack[-1]:
            self.stack.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.stack[-1]


# Main Call
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(-1)
obj.push(12)
obj.push(3)
obj.push(-4)

obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
