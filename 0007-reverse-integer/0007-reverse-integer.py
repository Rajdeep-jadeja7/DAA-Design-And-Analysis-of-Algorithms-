class Solution:
    def reverse(self, x: int) ->int:
        rev=0
        num=x
        if(num<0):
            num=abs(num)
               
        while(num>0):
            rev=rev*10 + num%10
            num//=10   
        
        else:
            if(rev>2147483647 or rev<(-2147483648)):
                return 0
            else:        
                if(x<0):
                  return -(rev)

                else:
                    return rev    




        