class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        evencount=0
        oddcount=0
        new=[]
        for i in nums:
            if i%2==0:
                evencount+=1
            else:
                oddcount+=1

        for j in range(evencount):
            new.append(0)
        for  k in range(oddcount):
            new.append(1)
        return new      
