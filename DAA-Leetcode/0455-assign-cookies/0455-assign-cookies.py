class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        i=0
        j=0
        count=0
        s.sort()
        g.sort()
        while (i<len(g) and j<len(s)):
            if s[j]>=g[i]: 
                i+=1
            j+=1    
        return i            
        
        