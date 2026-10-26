class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[]
        temp2=[]
        if k>len(nums):
            k=k%len(nums)
        temp=nums[n-k:]
        temp2=nums[:n-k]
        nums[:k]=temp
        nums[k:]=temp2
        return nums
      
        