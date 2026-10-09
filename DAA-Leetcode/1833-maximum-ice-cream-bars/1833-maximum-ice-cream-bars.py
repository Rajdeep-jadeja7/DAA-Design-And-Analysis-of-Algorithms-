class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count=0
        for i in costs:
            if i<=coins:
                count+=1
                coins-=i
        return count        

        