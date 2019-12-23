class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        l = len(nums)-1
        mid = len(nums)//2
        while i <= l:
            if nums[mid] == target:
                
            if target > nums[mid]:
                
                i = mid + 1
            else:
                l= mid - 1
            mid = (i+ l)//2
        return -1
        