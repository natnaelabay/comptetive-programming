# Natnael Abay

# se.natnael.abay@gmail.com

class MyQueue:
    def __init__(self):
        self.inn,self.out = [],[]
        

    def push(self, x):
        self.inn.append(x)

    def pop(self):
        self.peek()
        return self.out.pop()

    def peek(self):
        if not self.out:
            while self.inn:
                self.out.append(self.inn.pop())
        return self.out[-1]        

    def empty(self):
        return not self.inn and not self.out
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
