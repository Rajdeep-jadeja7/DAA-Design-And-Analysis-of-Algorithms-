class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k==len(s):
            return s[::-1]
        rev=s[:k:]    
        return  rev[::-1]+s[k:]
        