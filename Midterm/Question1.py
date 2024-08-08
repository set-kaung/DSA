# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

class heap:
    def compare(x, y):  
        return x < y
    
    def maxcompare(x,y):
        return x > y

    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < self.heapsize and self.cmp(self.a[l],self.a[i]):
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.cmp(self.a[r],self.a[largest]):
            largest = r
        if largest != i:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.heapify(largest)
        
    def insert(self, x):
        self.heapsize += 1
        if len(self.a) < self.heapsize:
            self.a.append(x)
        else:
            self.a[self.heapsize-1] = x
        i = self.heapsize-1
        j = (i-1)//2
        while i > 0 and self.cmp(self.a[i],self.a[j]):
            self.a[i],self.a[j] = self.a[j],self.a[i]
            i = j
            j = (i-1)//2

    def extract(self):
        x = self.a[0]
        last = self.heapsize-1
        self.a[0],self.a[last] = self.a[last],self.a[0]
        self.heapsize -= 1
        self.heapify(0)
        return x

    def buildHeap(self):
        for i in range((self.heapsize-1)//2, -1, -1):
            self.heapify(i)
            
    def __init__(self, items=[], cmp=compare):
        self.a = items
        self.cmp = cmp
        self.heapsize = len(self.a)
        if len(self.a) > 0:
            self.buildHeap()


M, N = map(int, input().split())
prices = list(map(int,input().split()))

h = heap(prices,heap.maxcompare)
total = 0
while N > 0:
    mx = h.extract()
    total += mx
    mx -= 1
    h.insert(mx)
    N -= 1
    
print(total)