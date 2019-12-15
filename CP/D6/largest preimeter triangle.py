# Natnael Abay

# se.natnael.abay@gmail.com
# i got a little help from senior freiends
import itertools
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        index = len(A) - 1
        while index-2 >= 0:
            if A[index] + A[index-1] > A[index-2] and A[index] + A[index-2] > A[index-1]  and A[index-1] + A[index-2] > A[index]:
                return A[index] + A[index-1] + A[index-2]
            index = index -1
        return 0
