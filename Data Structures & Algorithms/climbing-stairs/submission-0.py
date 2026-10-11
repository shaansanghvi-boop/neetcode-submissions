class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0, 1, 2]
        if n < 3:
            return table[n]
        for i in range(3, n + 1, 1):
            table.append(table[i-1] + table[i-2])
        return table[n]