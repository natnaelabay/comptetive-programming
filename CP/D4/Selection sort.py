# natnael abay
#se.natnael.abay@gmail.com
def selectionSort(lst):
   for i in range(len(lst)-1,0,-1):
       max=0
       for location in range(1,i+1):
           if lst[location]>lst[max]:
               max = location

       temp = lst[i]
       lst[i] = lst[max]
       lst[max] = temp

