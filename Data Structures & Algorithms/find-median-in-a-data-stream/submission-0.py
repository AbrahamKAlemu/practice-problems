import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        if self.maxHeap and self.maxHeap[0] * -1 > self.minHeap[0]:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val * -1)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            val = heapq.heappop(self.minHeap) * -1
            heapq.heappush(self.maxHeap, val)


    def findMedian(self) -> float:
        minVal = self.minHeap[0]
        maxVal = self.maxHeap[0] * -1 if self.maxHeap else 0
        if len(self.minHeap) == len(self.maxHeap):
            return (minVal + maxVal) / 2
        if len(self.minHeap) > len(self.maxHeap):
            return minVal
        return maxVal
        
        