class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        ret =[]

        for i in range(len(nums)):
            if table.get(target - nums[i], -1) != -1:
                return [table[target - nums[i]], i]
            table[nums[i]] = i
