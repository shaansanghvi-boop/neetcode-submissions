class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                res = 0
                x = int(stack.pop())
                y = int(stack.pop())
                if t == "+":
                    res = x + y
                if t == "*":
                    res = x * y
                if t == "/":
                    res = y / x
                if t == "-":
                    res = y - x
                stack.append(res)
            else:
                stack.append(int(t))
        return int(stack.pop())
                