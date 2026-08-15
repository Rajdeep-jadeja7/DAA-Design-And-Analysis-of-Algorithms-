class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=0
        if (len(s)!=len(t)):
            return False
        for ch in s:
            if ch in t:
                t=t.replace(ch,"",1)
                count+=1
        maximum=max(len(s),len(t))        
        
        if count==maximum:
            return True
        else:
            return False
             
        