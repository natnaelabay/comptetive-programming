# Natnael Abay

# se.natnael.abay@gmail.com

from collections import *
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hM = defaultdict(int)
        visited = set()
        for i in arr1:
            hM[i] +=1       
        lst = []       
        for j in arr2:
            lst.extend([j]*hM[j])
            visited.add(j)  
        leftover = sorted(set(hM.keys()).difference(visited))
        for j in leftover:
            lst.extend([j]*hM[j]) 
        return lst
