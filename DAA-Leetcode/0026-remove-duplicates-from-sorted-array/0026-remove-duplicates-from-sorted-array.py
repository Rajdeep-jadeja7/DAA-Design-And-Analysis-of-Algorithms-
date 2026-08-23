class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        k=0
        i=0
        j=0
        num=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)-1):
                if nums[i]==nums[j]:
                    k+=1
                    nums.remove(nums[j])
                    
        return len(nums)  

        """

        digits={}

        for i in nums:
            if i not in digits:
                digits[i]=1
        j=0        
        for k in digits.keys():        
            nums[j]=k  
            j+=1
        return j      




        