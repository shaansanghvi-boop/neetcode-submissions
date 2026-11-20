class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ret = []
        for x, y in points:
            d = (x**2 + y**2) * -1
            heapq.heappush(heap,[d, x, y])
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            d, x, y = heapq.heappop(heap)
            ret.append([x, y])
        return ret

        