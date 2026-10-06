class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        minimumsum=0
        if len(prices)>len(discounts):
            while(len(prices)!=len(discounts)):
                discounts.append(0)    

        fusedinput=list(zip(prices,discounts))    
        for i in fusedinput:
            minimumsum+=(i[0]*(100-i[1]))/100

        return minimumsum


        