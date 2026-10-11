class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [1]
        postprod = [1]

        for num in nums:
            preprod.append(num * preprod[-1])
        preprod.pop()
        for num in nums[::-1]:
            postprod.append(num * postprod[-1])
        postprod.pop()
        postprod.reverse()
        ret = []
        for i in range(len(postprod)):
            ret.append(preprod[i] * postprod[i])
        return ret

