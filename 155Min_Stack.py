"""
Description
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x)--Push element x onto stack.
pop()--Removes the element on top of stack.
top()--Get the top element.
getMin()--Retrieve the minimum element in the stack.

"""



class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minOfStack = list()
        
    def push(self, x):
        """
        :type x: int
        :rtype:void
        """
        self.stack.append(x)
        if not self.minOfStack or self.minOfStack[-1] >= x:
            self.minOfStack.append(x)
    def pop(self):
        """
        :rtype: void
        """
        v = self.stack.pop()
        if self.minOfStack and self.minOfStack[-1] == v:
            self.minOfStack.pop()
    
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.minOfStack[-1]