class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        maximum=nums[0]
        minimum=nums[0]
        instability=0


        for i in range(len(nums)):
            maximum=max(nums[:i+1],default=0)
        
            for j in range(i,len(nums)):
        
                minimum= min(nums[i:])
                instability= maximum - minimum
                if instability <= k:
                    return j
        return -1    
        
        """
        maximum=nums[0]
        minimum=nums[0]
        instability=0
        for i in range(len(nums)):
            if nums[i]>maximum:
                maximum=nums[i]
            for j in range(i,len(nums)):
                minimum=nums[i]
                if nums[j]<minimum:
                    minimum=nums[j]
                    instability = maximum - minimum
                    if instability <= k:
                        return j
        return -1  
        """  

        
        