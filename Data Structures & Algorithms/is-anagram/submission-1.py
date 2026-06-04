class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        return sorted(t) == sorted(s)