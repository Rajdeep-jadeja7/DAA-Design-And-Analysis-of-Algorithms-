class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=n
        sum1=0
        mul=1
        sum2=0
        while(num>0):
            sum1+=num %10
            mul*=num%10
            num//=10
        sum2=sum1+mul    
        if n%sum2==0:
            return True
        else:
            return False    



      
        