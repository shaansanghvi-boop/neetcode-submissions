class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        table = [float('inf')] * (amount + 1)
        table[0] = 0
        for i in range(amount + 1):
            for j in coins:
                if i - j >= 0:
                    table[i] = min(1 + table[i-j], table[i])

        return table[amount] if table[amount] != float('inf') else -1
                