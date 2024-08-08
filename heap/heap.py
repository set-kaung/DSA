def left(i):
    return (2*i)+1

def right(i):
    return (2*i)+2

class heap:
    def __init__(self, arr:list[int]) -> None:
        self.arr = arr
    
    def max_heapify(self,i):
        print(self.arr, self.arr[i])
        l = left(i)
        r = right(i)
        largest = i
        if l <= self.heap_size and self.arr[l] > self.arr[i]:
            largest = l
        if r <= self.heap_size and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)

    def build_maxheap(self):
         self.heap_size = len(self.arr)-1
         i = len(self.arr)//2
         while i >= 0:
            self.max_heapify(i)
            i -=1

             
    def sort(self):
        self.build_maxheap()
        i = len(self.arr)-1
        while i >= 1:
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.heap_size = self.heap_size - 1
            self.max_heapify(0)
            i -= 1


# a = list(map(int, input().split()))
a = [x for x in range(1,11)]
import time
st = time.process_time()

he = heap(a)
he.build_maxheap()
# he.sort()

et = time.process_time()

# print(a)
# print(et-st)
