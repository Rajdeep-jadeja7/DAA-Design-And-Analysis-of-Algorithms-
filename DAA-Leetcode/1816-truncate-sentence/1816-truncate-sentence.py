class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        s1=""
        s=s.split()
        for i in range(k):
            s1+=s[i]+" "
        return s1.strip()

        