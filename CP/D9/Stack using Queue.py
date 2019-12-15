# Natnael Abay

# se.natnael.abay@gmail.com




import collections import deque
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        a = self.que.pop()
        self.que.append(a)
        return a

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.que) == 0
        
