class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        counts = 0
        def dfs(row, col, count):
            if (row < 0 or col < 0 or row >= rows or col >= cols):
                return count
            if grid[row][col] == 1:
                count += 1
                grid[row][col] = 0
                count = dfs(row + 1, col, count)
                count = dfs(row, col + 1, count)
                count = dfs(row - 1, col, count)
                count = dfs(row, col - 1, count)
            return count

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    counts = max(counts, dfs(i, j, 0))
        
        return counts