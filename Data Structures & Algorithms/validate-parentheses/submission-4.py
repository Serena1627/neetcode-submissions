class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        i = 0
        while i < len(s):
            if s[i] not in pairs.keys():
                stack.append(s[i])
            else:
                if not stack or stack.pop() != pairs.get(s[i]):
                    return False
            i += 1
        if not stack:
            return True
        return False

        