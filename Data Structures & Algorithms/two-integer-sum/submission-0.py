class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        ret = []
        for i in range(len(nums)):
            if di.get(target - nums[i], -1) != -1:
                ret.append(di.get(target - nums[i]))
                ret.append(i)
                return ret
            di[nums[i]] = i
        return ret