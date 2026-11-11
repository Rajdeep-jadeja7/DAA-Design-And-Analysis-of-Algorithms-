class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:

        count=0
        ch=""
        for i in nums:
            ch=str(i)
            for c in ch:
                if str(digit)==c:
                    count+=1
        return count        
            
        