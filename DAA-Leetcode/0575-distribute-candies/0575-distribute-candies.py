class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candies={}
        count=0
        for i in candyType:
            if i not in candies:
                candies[i]=1
            else:
                candies[i]+=1
        unique=0
        for i in candies.keys():
            unique+=1

        count=len(candyType)//2 
        if count<=unique:
            return count
        else:
            return unique    




        