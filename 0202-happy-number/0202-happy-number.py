class Solution:
    def isHappy(self, n: int) -> bool:

        num=n
        rem=0
        square=0
        while(num>0):
            rem= num%10
            square+=(rem*rem)
            num//=10

        for i in range(0,10):
            if(square==1):
                return True
            else:
                num=square
                square=0
                while(num>0):
                    rem= num%10
                    print(rem)
                    square+=(rem*rem)
                    print(square)
                    num//=10  
        return False              







    
        