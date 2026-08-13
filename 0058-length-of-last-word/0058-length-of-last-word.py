class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s=s.strip()
        for i in s[::-1]:
            if  i !=" ":
                count+=1
            else:
                break    
        return count    
        