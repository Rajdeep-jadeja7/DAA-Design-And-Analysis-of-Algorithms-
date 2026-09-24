class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if nums[i]<10:
                if i==nums[i]:
                    return i
            elif(nums[i]>=10):
                sum1=0
                n=nums[i]
                while(n>0):
                    rem=n%10
                    sum1+=rem
                    n//=10
                if sum1==i:
                    return i 
        return -1           

        