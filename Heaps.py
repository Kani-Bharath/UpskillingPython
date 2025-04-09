#Heaps

import heapq

#Under the hood are arrays
minHeap=[]
heapq.heappush(minHeap,5)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)
heapq.heappush(minHeap,1)
heapq.heappush(minHeap,6)
heapq.heappush(minHeap,3)

print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

print(minHeap)


#No maxheap by default, work around is to
#use min heap and multiply by -1 when push and pop

maxHeap = []

heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

print(maxHeap)

#Max is always at index 0

print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))


#Build heap from inital values
arr=[2, 1, 8,4, 5]
heapq.heapify(arr)
print(arr)

while arr :
    print(heapq.heappop(arr))