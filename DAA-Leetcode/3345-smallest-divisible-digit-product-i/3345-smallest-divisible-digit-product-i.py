class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        

        if(n<10 and n<t):
            return t
        
        for i in range(0,10):
            num=n
            mul=1
            while(num>0):
                divisor=num%10
                mul*=divisor
                num//=10
            if(mul%t==0):
                return n 
            n+=1      

        
           




        