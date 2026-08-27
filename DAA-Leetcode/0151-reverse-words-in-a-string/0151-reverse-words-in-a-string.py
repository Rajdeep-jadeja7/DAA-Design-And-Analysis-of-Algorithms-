class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s1=""
        for i in range(len(s)-1,-1,-1):
            s1+=" " +s[i]
        s1=s1.strip()
        return s1