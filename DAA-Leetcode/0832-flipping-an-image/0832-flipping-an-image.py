class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        InvertImage=[]
        for i in image:
            temp=i[::-1]
            for j in range(len(temp)):
                if temp[j]==0:
                    temp[j]=1
                else:
                    temp[j]=0  
            InvertImage.append(temp)
        return InvertImage             
                      
        