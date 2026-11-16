class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dif = 0
        low = float('inf')
        for p in prices:
            dif = max(dif, p - low)
            low = min(low, p)
        return dif