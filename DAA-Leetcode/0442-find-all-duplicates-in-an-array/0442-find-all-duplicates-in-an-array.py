class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        count={}
        duplicates=[]

        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for k,v in count.items():
            if v==2:
                duplicates.append(k)

        return duplicates        

        