class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        unique=[]
        for i in nums:
            if i not in unique:
                unique.append(i)
        if len(unique)>=3:
            return unique[-3]
        else:
            return max(nums)

        