class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indexsum=0
        indexcommon=[]
        common=[]

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    indexsum = i+j
                    indexcommon.append([list1[i],indexsum])

   
        minimum=min(indexcommon,key=lambda x:x[1])  

        for i in range(len(indexcommon)):
            if indexcommon[i][1]==minimum[1]:
                common.append(indexcommon[i][0])
        
        return common                        


        