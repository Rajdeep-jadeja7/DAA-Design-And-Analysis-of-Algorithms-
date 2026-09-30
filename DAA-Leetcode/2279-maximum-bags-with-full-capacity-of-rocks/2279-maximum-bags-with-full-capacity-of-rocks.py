class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:

        fusedinput=zip(capacity,rocks)
        count=0
        Remaining=[]

        for c,r in fusedinput:
            Remaining.append(c-r)
        fusedinput2=sorted(zip(capacity,rocks,Remaining),key=lambda x:x[2])
        for i in fusedinput2:
            need=i[2]
            if need<=additionalRocks:
                additionalRocks-=need
                count+=1
        return count            
        