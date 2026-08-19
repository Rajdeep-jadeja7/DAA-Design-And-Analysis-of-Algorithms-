class Solution:
    def isPalindrome(self, x: int) -> bool:

        num=x
        rev=0

        while(num>0):
            rev = rev *10 + num%10
            num//=10
        if(rev==x):
            return True
        else:
            return False        
        