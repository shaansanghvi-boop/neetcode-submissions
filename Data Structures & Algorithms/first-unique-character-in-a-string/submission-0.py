class Solution:
    def firstUniqChar(self, s: str) -> int:
        frqs = {}

        for char in s:
            frqs[char] = frqs.get(char, 0) + 1
        i = 0
        for char in s:
            if frqs[char] == 1:
                return i
            i = i + 1
        return -1