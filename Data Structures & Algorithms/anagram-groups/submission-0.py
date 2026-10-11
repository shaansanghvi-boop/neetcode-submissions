class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            sword = ''.join(sorted(word))
            res[sword].append(word)
        return list(res.values())