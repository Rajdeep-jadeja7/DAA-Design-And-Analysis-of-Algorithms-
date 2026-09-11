class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if (len(nums)==1):
            return False
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False        

       


        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                   return True

        return False            
        """       
        