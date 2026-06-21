import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for n in gifts:
            heapq.heappush(heap, n * -1)
        for i in range(k):
            val = heapq.heappop(heap)
            total = math.floor(math.sqrt(val * -1 ))
            heapq.heappush(heap, total * - 1)
        
        return sum(heap) * -1
        