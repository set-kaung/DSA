from Heap import heap

ropes = list(map(int, input().split()))

h = heap(ropes)

accsum = 0

while h.heapsize > 1:
    first = h.extract()
    second = h.extract()
    leg = first + second
    accsum += leg
    h.insert(leg)

print(accsum)