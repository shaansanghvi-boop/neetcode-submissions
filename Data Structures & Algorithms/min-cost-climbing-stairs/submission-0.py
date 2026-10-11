class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        table = [1] * len(cost)
        table[len(cost) - 1] = cost[len(cost) - 1]
        table[len(cost) - 2] = cost[len(cost) - 2]
        for i in range(len(cost) - 3, -1, -1):
            table[i] = min(table[i+1], table [i+2]) + cost[i]
        return min(table[0], table[1])

