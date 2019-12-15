# natnael abay
# se.natnael.abay@gmail.com
import random
def QuickSort( A, low, high ):
    if low < high:
        pivot = Partition( A, low, high)
        QuickSort( A, low, pivot - 1 )

        QuickSort( A, pivot + 1, high)
    return A
def Partition( A, low, high ) :
    pivot= low
    swap(A, pivot, high)
    for i in range(low, high ):
        if A[i] <=A[high]:
            swap( A, i, low)
            low+=1
    swap( A, low, high)
    
    return low
def swap( A, x, y ):
    temp= A[x]
    A[x] = A[y]
    A[y] = temp
A= [3,2,1,4]
c = QuickSort(A, 0, len( A ) - 1)
print(c)
