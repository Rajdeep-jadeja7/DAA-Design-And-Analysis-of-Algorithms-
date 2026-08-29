class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        s1=""
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        for k,v in sorted(freq.items(),key=lambda x:x[1],reverse=True):
            s1+=k*v

        return s1                
        