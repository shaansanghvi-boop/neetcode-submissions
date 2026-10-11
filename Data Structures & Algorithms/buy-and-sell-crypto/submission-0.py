class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dif = 0
        lmin = prices[0]

        for num in prices:
            dif = max(dif, num - lmin)
            lmin = min(lmin, num)
        return dif