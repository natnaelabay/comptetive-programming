# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left = 0 
        right = n-1
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
        
        
        
        
        # i = 1
        # count = 0
        # s = 0
        # stack = []
        # while i <= n:
        #     if isBadVersion(i):
        #         return i
        #     else:
        #         i+=1 