class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [1] * len(nums)
        postprod = [1] * len(nums)
        ret = []

        for i in range(1, len(nums)):
            preprod[i] = nums[i-1] * preprod[i-1]
        for i in range(len(nums) - 2, -1, -1):
            postprod[i] = nums[i+1] * postprod[i+1]
        for i in range(len(nums)):
            ret.append(preprod[i] * postprod[i])
        return ret

