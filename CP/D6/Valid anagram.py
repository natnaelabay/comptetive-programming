# Natnael Abay

# se.natnael.abay@gmail.com

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0 
        s = [char for char in s]
        s.sort()
        t  = [char for char in t]
        t.sort()
        if s == t:
            return True
        else:
            return False
