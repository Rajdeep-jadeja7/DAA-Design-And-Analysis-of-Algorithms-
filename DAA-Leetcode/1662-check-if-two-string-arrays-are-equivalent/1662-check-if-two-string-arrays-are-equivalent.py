class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        fullword1=""
        fullword2=""
        if len(word1)>1:
            for i in word1:
                fullword1+=i
        else:
            fullword1=word1[0]        
        if len(word2)>1:
            for j in word2:
                fullword2+=j
        else:
            fullword2=word2[0]     
        if fullword1==fullword2:
            return True
        else:
            return False           



        