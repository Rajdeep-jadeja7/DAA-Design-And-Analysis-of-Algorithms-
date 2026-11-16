class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages=[]
        while len(nums)!=0:
            minnum=min(nums)
            maxnum=max(nums)
            averages.append((minnum+maxnum)/2)
            nums.remove(minnum)
            nums.remove(maxnum)
        return min(averages)    
        
        