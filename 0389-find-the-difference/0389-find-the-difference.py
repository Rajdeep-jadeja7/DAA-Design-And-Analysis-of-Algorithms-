class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n=""
        for i in t:
            if i in s:
                s=s.replace(i,"",1)
            else:    
                 n+=i
        return n       

        