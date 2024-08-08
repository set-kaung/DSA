
def mergeSort(A:list[int], start:int,end:int):
    if start < end:
        mid = (start+end)//2
        mergeSort(A,start,mid)
        mergeSort(A,mid+1,end)
        merge(A,start,mid,end)




def merge(A:list[int],start:int,mid:int,end:int):
    left, right = (A[start:mid+1]).copy(), (A[mid+1:end+1]).copy()
    i,j = 0,0
    k = start
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            k += 1
            i += 1
        else:
            A[k] = right[j]
            k += 1
            j += 1
    
    while i < len(left):
        A[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        A[k] = right[j]
        k += 1
        j += 1

    
arr:list[int] = [3,0,5,1,6,2,7,10]

mergeSort(arr,0,len(arr)-1)
print(arr)