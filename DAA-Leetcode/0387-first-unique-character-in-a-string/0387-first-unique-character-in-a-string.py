class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique={}

        for i in s:
            if i not in unique:
                unique[i]=1
        for i in unique.keys():
            if s.count(i)==1:
                return s.index(i)
        return -1        