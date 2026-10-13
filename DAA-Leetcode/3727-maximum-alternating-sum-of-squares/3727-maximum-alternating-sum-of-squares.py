class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        square=[]
        for i in nums:
            square.append(i**2)
        square.sort()
        mid=len(square)//2 
        sum1=sum(square[:mid])
        sum2=sum(square[mid:])
        return sum2 - sum1   