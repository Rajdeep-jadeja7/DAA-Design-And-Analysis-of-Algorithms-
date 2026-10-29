class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        new=[]
        for i in matrix:
            count=0
            for j in i:
                if j==1:
                    count+=1
            new.append(count)    
        return new

        