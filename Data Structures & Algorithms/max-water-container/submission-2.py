class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        val = 0
        while l < r:
            low = min(heights[l], heights[r])
            val = max(val, low * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return val