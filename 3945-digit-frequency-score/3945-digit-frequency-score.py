class Solution:
    def digitFrequencyScore(self, n: int) -> int:

        num=n
        square=0
        while(num>0):
            rem=num%10
            square += rem
            num//=10
        return square    
        