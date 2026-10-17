class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        distinct=[]
        characters=[]
        count=0
        count2=0
        for i in words:
            for j in i:
                if j not in allowed:
                    count=1
                    break
                else:
                    count=0    
            if count!=1:
                count2+=1        
        return count2             
