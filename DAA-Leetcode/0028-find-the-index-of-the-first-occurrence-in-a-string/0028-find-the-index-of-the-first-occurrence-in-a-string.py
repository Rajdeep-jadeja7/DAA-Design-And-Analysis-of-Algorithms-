class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length=len(needle)
        if needle not in haystack:
            return -1
            
        else:
            for ch in range(len(haystack)):
                for i in needle:
                    if i == haystack[ch]:
                        if needle in haystack[ch:ch+length]:
                        
                            return ch

        