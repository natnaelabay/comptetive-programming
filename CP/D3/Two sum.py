# natnael abay
#se.natnael.abay@gmail.com
def twoSum(nums, target):
    all = {}
    for index, num in enumerate(nums):
        other = target - num 
        if other in all:
            return [all[other], index]
        else:
            all[num] = index                
    return []
