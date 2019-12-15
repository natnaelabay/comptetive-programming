# natnael abay
#se.natnael.abay@gmail.com
def insertionSort(lst):
   for i in range(1,len(lst)):
       current = lst[i]
       while lst[i-1]>current and i>0:
           lst[i] = lst[i-1]
           i = i-1
           lst[i] = current
   return lst

print(insertionSort([5,2,1,9,0,4,6]))
