# natnael abay
#se.natnael.abay@gmail.com
import math
class Solution:
    def reverse(self, x: int) -> int:
        if x>=(-1*math.pow(2,31)) and x<=(math.pow(2,31)-1):  
            f = str(x)
            if '-' in f:
                f = f.strip('-')
                f = f[::-1]
                if int(f)>=(-1*math.pow(2,31)) and int(f)<=(math.pow(2,31)-1):
                    return int(f)*-1
                else:
                    return 0
            else:
                f = f[::-1]
                if int(f)>=(-1*math.pow(2,31)) and int(f)<=(math.pow(2,31)-1):
                    return int(f)
                return 0
        else:
            return 0
            
            
        
     
