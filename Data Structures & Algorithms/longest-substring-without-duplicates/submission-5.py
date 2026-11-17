class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1
        l, r = 0, 1
        ret = 0
        running = set()
        running.add(s[l])
        while r < len(s):
            if s[r] not in running:
                running.add(s[r])
                r += 1
                ret = max(ret, r - l)
            else:
                while s[r] in running:
                    running.remove(s[l])
                    l += 1
        return ret

        