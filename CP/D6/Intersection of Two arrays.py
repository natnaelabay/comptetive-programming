# Natnael Abay

# se.natnael.abay@gmail.com

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            boolean = True
            for j in nums2:
                if i == j:
                    boolean = False
            if not boolean:
                ans.append(i)
        return list(set(ans))
