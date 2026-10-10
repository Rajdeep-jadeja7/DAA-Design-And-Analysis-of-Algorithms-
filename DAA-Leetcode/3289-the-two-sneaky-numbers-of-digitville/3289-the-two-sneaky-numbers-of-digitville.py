class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        Mischievious=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]==nums[j]:
                    if nums[i] not in Mischievious:
                        Mischievious.append(nums[i])


                if  len(Mischievious)==2:
                    return Mischievious     
