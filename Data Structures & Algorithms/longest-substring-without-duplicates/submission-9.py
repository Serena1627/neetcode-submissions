class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        letters = []
        while right < len(s):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.append(s[right])
            right += 1
            longest = max(longest, len(letters))
        return longest
            