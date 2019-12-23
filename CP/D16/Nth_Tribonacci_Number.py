class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            a = 0
            b = 1
            d = 1
            c = 0
            while(n>2):
                c= a + b +d
                a = b
                b = d
                d = c    
                n=n-1
            return c