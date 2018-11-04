'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
'''

import collections
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myqueue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self.myqueue
        q.append(x)
        for i in range(0, len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.myqueue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.myqueue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.myqueue)
