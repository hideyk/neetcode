from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for l in s:
            seen[l] += 1
        for l in t:
            seen[l] -= 1
        
        for l, cnt in seen.items():
            if cnt != 0:
                return False
        return True