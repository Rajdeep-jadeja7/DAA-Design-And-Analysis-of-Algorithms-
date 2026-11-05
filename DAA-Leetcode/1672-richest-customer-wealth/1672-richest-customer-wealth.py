class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        maxsum=0
        for i in accounts:
            sum1=0
            j=i
            for k in j:
                sum1+=k
            if sum1>maxsum:
                maxsum=sum1
        return maxsum                

        