'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack(object):

    def __init__(self):

        self.stacklist = []
        self.minimumElement = float('inf')

    def push(self, x):

        self.stacklist.append(x)
        if x < self.minimumElement:
            self.minimumElement = x

    def pop(self):

        last_val = self.stacklist[-1]

        if self.minimumElement == last_val:
            self.minimumElement = float('inf')

            for i in range(0, len(self.stacklist) - 1):
                if self.stacklist[i] < self.minimumElement:
                    self.minimumElement = self.stacklist[i]

        return self.stacklist.pop(-1)

    def top(self):

        return self.stacklist[-1]

    def getMin(self):

        return self.minimumElement