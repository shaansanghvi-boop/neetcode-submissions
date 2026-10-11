class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        if not digits:
            return ret
        reverse = digits[::-1]
        carry = 1
        for num in reverse:
            digit = num + carry
            carry = digit // 10
            digit = digit % 10
            ret.append(digit)
        if carry:
            ret.append(1)
        ret.reverse()
        return ret