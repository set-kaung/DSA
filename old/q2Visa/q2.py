a = [21,26,36,17,29]

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i + 1
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def make_reservation(arr,k,t):
    postion = len(arr)
    for i in range(len(arr)):
        j = i + 1
        while j > 0 and abs(t-arr[postion]) >= k:
            

    

insertion_sort(a)

print(a)