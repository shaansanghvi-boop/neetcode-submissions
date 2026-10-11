class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row, col):
            if (row < 0 or col < 0 or row >= rows or col >= cols):
                return
            if grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row + 1, col)
                dfs(row, col + 1)
                dfs(row - 1, col)
                dfs(row, col - 1)
            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count
