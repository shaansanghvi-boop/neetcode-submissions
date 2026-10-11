class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = defaultdict(int)
        set2 = defaultdict(int)
        len1 = len(s)
        len2 = len(t)
        if len1 != len2:
            return False
        for i in range(len1):
            set1[s[i]] = set1[s[i]] + 1
            set2[t[i]] = set2[t[i]] + 1
        if set1 == set2:
            return True
        return False
