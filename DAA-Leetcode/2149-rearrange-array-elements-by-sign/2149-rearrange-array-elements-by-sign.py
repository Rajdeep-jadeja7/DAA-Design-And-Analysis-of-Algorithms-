class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        negative=[]
        positive=[]
        Rearranged_array=[]
        for i in nums:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)
        for i in range(len(positive)):
            Rearranged_array.append(positive[i])
            Rearranged_array.append(negative[i])
        return Rearranged_array    
        