class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        
        mintotaltime=1000
        for i in tasks:
            totaltime=0
            temp=i
            for j in temp:
                totaltime+=j
            if totaltime<mintotaltime:
                mintotaltime=totaltime
        return mintotaltime            

        