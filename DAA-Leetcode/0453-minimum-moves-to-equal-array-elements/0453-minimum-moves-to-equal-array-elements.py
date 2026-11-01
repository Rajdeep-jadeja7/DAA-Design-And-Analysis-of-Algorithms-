class Solution:
    def minMoves(self, nums: list[int]) -> int:
        unique_count=len(set(nums))
        if unique_count==1:
            return 0
        minimum=min(nums)    
        sum1=0
        for i in nums:
            sum1+=i-minimum

        return sum1
        