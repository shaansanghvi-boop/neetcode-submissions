class Solution:
    def trap(self, height: List[int]) -> int:
        suf = [0] * (len(height) + 1)
        pre = [0] * (len(height) + 1) 
        for i in range(1, len(height)):
            pre[i] = max(height[i-1], pre[i-1])
        for i in range(len(height) -2, -1, -1):
            suf[i] = max(height[i+1], suf[i+1])
        res = 0
        for i in range(len(height)):
            res += max(0, min(suf[i], pre[i]) - height[i])
        return res