class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}

        for i in range(len(nums)):
            if table.get(nums[i], False):
                return True
            table[nums[i]] = True
        return False
