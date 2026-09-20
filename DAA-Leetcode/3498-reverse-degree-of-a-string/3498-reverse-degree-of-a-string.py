class Solution:
    def reverseDegree(self, s: str) -> int:
        letters={}
        j=97
        for i in range(26,0,-1):
            letters[chr(j)]=i
            j+=1
        degree=0
        count=1
        for i in range(len(s)):
            char=s[i]
            for k,v in letters.items():
                if k==char:
                    degree+=count*v
            count+=1        
        return degree            



        