# Natnael Abay

# se.natnael.abay@gmail.com

class Stack:
    def __init__(self):
        self.data = []
    def push(self,a):
        self.data.append(a)
    def pop(self):
        self.data.pop()
class Solution:
    def isValid(self, myStr: str) -> bool:
        open_list = ["[","{","("] 
        close_list = ["]","}",")"] 
        stack = []
        for i in myStr: 
            if i in open_list: 
                stack.append(i) 
            elif i in close_list: 
                pos = close_list.index(i) 
                if ((len(stack) > 0) and
                    (open_list[pos] == stack[-1])): 
                    stack.pop() 
                else: 
                    return False
        if len(stack) == 0:
            return True
