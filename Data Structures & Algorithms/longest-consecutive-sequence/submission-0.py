class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ret = 0
        for num in seen:
            if num - 1 in seen:
                continue
            else:
                l = 0
                while l + num in seen:
                    l += 1
                ret = max(l, ret)
        return ret
