class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        count=0
        rows=0
        while(n>0):
            n-=i
            rows=i
            count+=1
            if n<=rows:
                return count
          
            i+=1
        return count    

        