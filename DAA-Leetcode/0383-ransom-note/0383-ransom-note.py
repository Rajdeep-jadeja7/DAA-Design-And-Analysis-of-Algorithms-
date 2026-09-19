class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        occurence1={}
        occurence2={}
        for i in ransomNote:
            if i not in occurence1:
                occurence1[i]=1
            else:
                occurence1[i]+=1
        for i in magazine:
            if i not in occurence2:
                occurence2[i]=1
            else:
                occurence2[i]+=1        
    
        if ransomNote in magazine:
            return True
        return False 
        """
        for i in magazine:
            if i in ransomNote:
                ransomNote=ransomNote.replace(i,"",1)  
        if ransomNote=="":
            return True
        return False             
        