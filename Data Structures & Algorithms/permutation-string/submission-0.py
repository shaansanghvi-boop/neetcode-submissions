class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        freq1 = {}
        freq2 = {}

        for char in s1:
            freq1[char] = freq1.get(char, 0) + 1

        for i in range(n1):
            char = s2[i]
            freq2[char] = freq2.get(char, 0) + 1

        for i in range(n1, n2):
            if freq1 == freq2:
                return True

            # Add right character
            add_char = s2[i]
            freq2[add_char] = freq2.get(add_char, 0) + 1

            # Remove left character
            remove_char = s2[i - n1]
            freq2[remove_char] -= 1
            if freq2[remove_char] == 0:
                del freq2[remove_char]  # Critical to delete 0-count keys for equality check

        return freq1 == freq2