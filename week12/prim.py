# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

V,E = map(int, input().split())
edgeList = []
adj_list = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

class heap:
    def compare(x, y):  # a default compare function for min heap
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

def cmpM(i,j):
    return i[2] < j[2]

def Prim(V,adj_list) -> int:
    total_weight = 0
    visited = set()

    visited.add(0)
    h = heap(cmp=cmpM)

    for v,w in adj_list[0]:
        h.insert((0,v,w))

    while len(visited) < V and not h.empty():
        u,v,w = h.extract()
        if v not in visited:
            total_weight += w
            visited.add(v)

            for to,weight in adj_list[v]:
                if to not in visited:
                    h.insert((v,to,weight))
    
    return total_weight

print(Prim(V,adj_list=adj_list))







