# Natnael Abay

# se.natnael.abay@gmail.com
def vals(nums):
    nums = nums.split()
    nums = [int(char) for char in nums]
    
    vis = []
    if len(nums) == 1:
        print(1)
    elif len(nums) ==2:
        print(11)
    else:
        for i in range(len(nums)):
            vis.append(0)
            
        for i in range(len(nums)):
             vis[nums[i]-1] = i
        min = vis[0]
        max = vis[0]
        beauti = []
        beauti.append(1)
        for i in range(1,len(vis)):
              if vis[i] < min:
                  min = vis[i]
              elif vis[i] >max:
                  max = vis[i]
              if (max - min) == i:
                  beauti.append(1)
              else:
                  beauti.append(0)
        beauti = [str(char) for char in beauti]
        print("".join(beauti))
 
c = []
a = int(input())
for i in range(a):
    inp = eval(input())
    val = input()
    c.append(val)
 
for i in range(a):
    vals(c[i])
            
 
