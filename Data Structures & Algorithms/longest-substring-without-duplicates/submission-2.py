class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        tmp = 0
        mp = {}
        
        for i in range(len(s)):
            if mp.get(s[i], -1) != -1 and mp[s[i]] >= l:
                l = mp[s[i]] + 1
                tmp = i - l + 1
                mp[s[i]] = i
            else:
                mp[s[i]] = i
                tmp += 1
            res = max(res, tmp)
        return res

