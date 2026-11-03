class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sum1=0
        maximum=max(nums)
        for i in nums:
            sum1+=maximum-i
        return sum1   
        