class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        
        for num in nums:
            freqs[num] += 1
        ret = []
        for num, count in freqs.items():
            ret.append([count, num])
        ret.sort()
        res = []
        while len(res) < k:
            res.append(ret.pop()[1])
        return res
         

