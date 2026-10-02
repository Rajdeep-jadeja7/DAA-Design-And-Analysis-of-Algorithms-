class Solution:
    def largestOddNumber(self, num: str) -> str:
        #n=int(num)
        j=-1
        for i in num:
            if int(num[j])%2==0:
                num=num[:j]
            else:
                return num  
        return num          
        """
        if int(num[-1])%2==0:
            num=num[:len(num-1)]
            if int(num[-1])%2==0:

        """
        """
            while(n>0):
                n//=10
                if(n%2!=0):
                    return str(n)
    
            """    
            #return ""    
        
          
        """    
        else:
            temp=0    
            while(n>0):
                temp+=n//10
                n//=10
            if temp%2!=0:
                return str(temp)
                """



        