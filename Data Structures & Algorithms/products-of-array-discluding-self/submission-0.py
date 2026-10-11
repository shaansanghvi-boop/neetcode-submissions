class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [1] * len(nums)
        sufprod = [1] * len(nums)
        res = []
        for i in range(1, len(nums)):
            preprod[i] = preprod[i-1] * nums[i-1]
        for j in range(len(nums) -2, -1, -1):
            sufprod[j] = sufprod[j+1] * nums[j+1]
        for i in range(len(nums)):
            val = sufprod[i] * preprod[i]
            res.append(val)
        return res
