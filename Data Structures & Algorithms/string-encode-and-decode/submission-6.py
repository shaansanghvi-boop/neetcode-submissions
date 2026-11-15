class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s))
            ret+= "#"
            ret += s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            x = int(num)
            i += 1
            ret.append(s[i:x + i])
            i += x
        return ret