class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if one != two:
                one = one - two
                heapq.heappush(stones, one)
        return stones[0] * -1 if stones else 0
            
