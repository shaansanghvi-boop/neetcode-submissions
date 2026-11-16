class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frq1 = defaultdict(int)
        frq2 = defaultdict(int)

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            frq1[s[i]] += 1
            frq2[t[i]] += 1
        return True if frq1 == frq2 else False