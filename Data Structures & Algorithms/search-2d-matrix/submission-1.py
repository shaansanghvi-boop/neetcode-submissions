class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2
            med = matrix[mid][0]
            if med == target:
                return True
            elif target < med:
                bot = mid - 1 
            else:
                top = mid + 1 
        right = len(matrix[bot]) - 1
        left = 0 
        while left <= right:
            mid = (left + right) // 2
            med = matrix[bot][mid]
            if target == med:
                return True
            elif target < med:
                right = mid -1
            else:
                left = mid +1
        return False