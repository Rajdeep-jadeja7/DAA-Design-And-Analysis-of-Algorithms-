class Solution:
    def countCommas(self, n: int) -> int:

        if n<=999:
            return 0  
        i=1000
        count=0
        while(i<=n):
        
            count += (n-i)+1
            i*=1000
        return count    
        