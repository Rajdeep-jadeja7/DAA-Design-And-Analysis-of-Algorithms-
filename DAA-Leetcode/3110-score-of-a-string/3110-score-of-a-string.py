class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        score1=0
        for i in range(len(s)-1):
            score1=ord(s[i])-ord(s[i+1])
            if score1<0:
                score1=-(score1)
            score+=score1    
            #score+=abs(ord(s[i])-ord(s[i+1]))
        return score    

        


        