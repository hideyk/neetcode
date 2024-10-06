class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                idx = r - len(charSet)
                charSet.remove(s[idx])
            charSet.add(s[r])
            res = max(res, len(charSet))
        return res