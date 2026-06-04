class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left = 0
        right = 0
        longest = 0
        letters = set()
        while right < len(s):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            right += 1
            longest = max(longest, right-left)
        return longest
        