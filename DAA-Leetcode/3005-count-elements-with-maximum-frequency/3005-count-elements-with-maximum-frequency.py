class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        digits={}
        if(len(nums)==1):
            return 1
        for num in nums:
            if num in digits:
                digits[num]+=1
            else:
                digits[num]=1
        count=[]

        for value in digits.values():
            count.append(value)


        maximum=0
        for value in count:
            if value>maximum:
                maximum=value
            
        max_freq=0
        for i in count:
            if i == maximum:
                max_freq+=maximum

        return max_freq       



        