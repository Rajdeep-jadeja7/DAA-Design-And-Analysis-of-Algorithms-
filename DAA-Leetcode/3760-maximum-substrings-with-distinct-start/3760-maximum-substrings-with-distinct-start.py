class Solution:
    def maxDistinct(self, s: str) -> int:
        unique=""
        for ch in s:
            if ch not in unique:
                unique+=ch
        return len(unique)        
