class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sum1=0
        diff=0
        num=0
        sum2=0
        for i in range(len(nums)):
            if nums[i]%3!=0:
                diff=3*(nums[i]//3)
                sum1=3*((nums[i]//3)+1)
                num=min(nums[i]-diff,sum1-nums[i])
                sum2+=num
        return sum2       




        