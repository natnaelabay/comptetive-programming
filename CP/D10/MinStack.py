# Natnael Abay

# se.natnael.abay@gmail.com




class MinStack:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
          
        ## the added elements are tuples the first is the element and the second is the current min at 
        ## during the addition of that element
        
        """Push element x onto stack"""
        min = x
        if self.data:
            current_min = self.getMin()
            if x < current_min:
                min = x
            else:
                min = current_min

        self.data.append((x, min))

    def pop(self) -> None:
        """Remove element on top of stack"""
        if self.data:
            return self.data.pop()[0]

    def top(self) -> int:
        """Get the top element e.g. peek"""
        if self.data:
            return self.data[-1][0]

    def getMin(self) -> int:
        """Retrieve the min"""
        if self.data:
            return self.data[-1][1]
