class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        uncommon=[]
        nonrepeatingwords=[]
        string1=s1.split()
        string2=s2.split()

        word_count1 = Counter(string1)
        word_count2=Counter(string2)
        for k,v in word_count1.items():
            if v<=1:
                nonrepeatingwords.append(k)

        for k,v in word_count2.items():
            if v<=1:
                nonrepeatingwords.append(k)        

        for i in string1:
            for j in string2:
                if j in nonrepeatingwords:
                    if j not in string1 and j not in uncommon:
                        uncommon.append(j)
                if i in nonrepeatingwords:
                    if i not in string2 and i not in uncommon:
                        uncommon.append(i)
        return uncommon                




        