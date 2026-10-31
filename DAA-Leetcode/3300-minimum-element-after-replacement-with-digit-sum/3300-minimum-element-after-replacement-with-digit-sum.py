class Solution:
    def minElement(self, nums: List[int]) -> int:
        temp=0
        sumofdigits=0
        for i in range(len(nums)):
            temp=nums[i]
            sumofdigits=0
            while(temp>0):
                  sumofdigits+=temp%10
                  temp//=10
            nums[i]=sumofdigits
        return min(nums)    
