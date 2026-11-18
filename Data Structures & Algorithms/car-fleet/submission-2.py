class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ts = []
        for i in range(len(speed)):
            ts.append((position[i], speed[i]))
        ts.sort(reverse=True)
        
        for p, s in ts:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
