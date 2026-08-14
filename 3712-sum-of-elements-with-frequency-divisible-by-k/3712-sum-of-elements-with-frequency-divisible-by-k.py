class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        freq={}
        count=0
        sum=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1 

        for key,value in freq.items():
            if value % k == 0:
                sum+=key * value
        return sum        

        