class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for _ in range(n)] for _ in range(m)]
        table[m-1][n-1] = 1
        # table [i][j] = amount of ways to get there from i, j
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j == n-1:
                    table[i][j] = 1
                elif i == m-1:
                    table [i][j] = 1
                else:
                    table[i][j] = table[i+1][j] + table[i][j+1]
        return table[0][0]