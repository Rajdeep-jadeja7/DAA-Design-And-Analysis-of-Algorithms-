class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count=0
        expected=sorted(heights)
        #expected=heights
        for i in range(len(expected)):
            if expected[i]!=heights[i]:
                count+=1
        return count        

        