class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        indexes=[]
        for i in range(len(nums)):
            if nums[i]==target:
                indexes.append(i)
        return indexes        
        