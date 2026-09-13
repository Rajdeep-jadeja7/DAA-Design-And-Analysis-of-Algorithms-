class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        sum1=0
        operations=0
        for i in nums:
            sum1+=i
        """    
        if sum1%k==0:
            return operations
        i=1
        while(i*k<sum1):
            k*=i
            i+=1
        return sum1%k    
        """
        operations = sum1 % k
        return operations
        


               
        