class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = {"{": "}", "[": "]", "(" : ")"}


        for char in s:
            if char in op:
                stack.append(char)
            else:
                if len(stack) == 0 or op[stack.pop()] != char:
                    return False
        if len(stack) == 0:
            return True
        return False
            