class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        prices.sort()
        original=money
        count=0
        sum1=0
        for i in prices[:2]:
            sum1+=i
            if sum1<=original:
                count+=1
                money-=i
        if count>=2:
            return money
        else:
            return original           
            


        