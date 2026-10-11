class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        water = 0

        while left < right:
            height = min(heights[left], heights[right])
            cont = height * (right - left)
            if cont > water:
                water = cont
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return water