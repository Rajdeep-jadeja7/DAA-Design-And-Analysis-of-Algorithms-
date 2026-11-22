class Solution:
    def checkString(self, s: str) -> bool:
        firstbindex=-1
        for i in range(len(s)):
            if s[i]=="b":
                firstbindex=i
                break
        if firstbindex!=-1 and 'a' in s[firstbindex:]:
            return False
        else:
            return True            

        