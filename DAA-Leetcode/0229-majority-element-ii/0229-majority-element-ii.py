class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        repeat=[]
        n=len(nums)
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for k,v in count.items():
            if v>n//3:
                repeat.append(k)
        return repeat       

        