class Solution:
    def minDeletion(self, s: str, k: int) -> int:

        freq={}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        distinct=len(freq)
        remove=0       
        if distinct==k:
            return 0
        else:    
            sorted_freq=dict(sorted(freq.items(),key=lambda item:item[1]))
            for key,value in sorted_freq.items():
                if distinct>k:
                    remove+=value
                    distinct-=1
        return remove            

