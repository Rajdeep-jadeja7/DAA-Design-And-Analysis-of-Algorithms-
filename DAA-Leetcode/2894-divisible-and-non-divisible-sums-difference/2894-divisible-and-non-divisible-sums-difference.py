class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible=[]
        notdivisible=[]
        sumdivisible=0
        sumnotdivisible=0
        for i in range(1,n+1):
            if i % m == 0:
                divisible.append(i)
                sumdivisible+=i
            else:
                notdivisible.append(i)
                sumnotdivisible+=i
        return sumnotdivisible-sumdivisible
                   

        