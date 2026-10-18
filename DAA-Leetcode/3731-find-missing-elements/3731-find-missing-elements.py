class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        nums.sort()
        missing=[]
        minimum=nums[0]
        maximum=nums[-1]
        count=minimum
        while(count!=maximum):
            if count not in nums:
                missing.append(count)
            count+=1
        return missing    

        """
        first=nums[0]
        last=nums[-1]
        count=first
        missing=[]
        for i in range(1,len(nums)-1):
            if nums[i]!=count+1:
                missing.append(count+1)
                count+=1
            else:
                count+=1    
        return missing        
        """
        """
        count=first
        missing=[]
        for i in nums:
            if i!=count:
                missing.append(i)
                count+=1
            else:
                count+=1   
        return missing         
        """
            

            

        