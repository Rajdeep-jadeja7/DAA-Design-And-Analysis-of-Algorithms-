class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        allalphabets="abcdefghijklmnopqrstuvwxyz"

        for  i in sentence:
            if i in allalphabets:
                allalphabets=allalphabets.replace(i,"",1)
        if allalphabets=="":
            return True
        else:
            return False            
        