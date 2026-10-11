class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())
        right = len(clean) - 1
        left = 0

        while left <= right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        return True