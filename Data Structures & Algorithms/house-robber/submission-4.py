class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) < 3:
            return max(nums[0], nums[1])
        table = [0] * len(nums)
        table[len(nums) -1] = nums[-1]
        table[len(nums) - 2] = max(nums[len(nums) - 2], nums[-1])
        for i in range(len(nums) - 3, -1, -1):
            table[i] = max(table[i+1], table[i+2] + nums[i])
        return max(table[0], table[1])