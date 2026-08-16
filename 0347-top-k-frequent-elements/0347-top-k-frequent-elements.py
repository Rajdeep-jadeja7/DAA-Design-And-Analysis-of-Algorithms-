class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        digits={}
        freq_elements=[]
        for num in nums:
            if num in digits:
                digits[num]+=1
            else:
                digits[num]=1
        keys=sorted(digits,key=digits.get,reverse=True)
        return keys[:k]     

        