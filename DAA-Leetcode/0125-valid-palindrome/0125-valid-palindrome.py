class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1=""
        
        for ch in (s.lower()):
            
            if (ch>="a" and ch<="z") or (ch>='0' and  ch<='9'):
                s1+=ch


        s1.strip()    
        if s1==s1[::-1]:
            return True
        else:
             return False    
        