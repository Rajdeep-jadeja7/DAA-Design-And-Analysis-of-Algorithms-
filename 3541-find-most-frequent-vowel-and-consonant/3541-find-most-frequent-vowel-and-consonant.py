class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel=[]
        consonant=[]
        vowels_count=[]
        consonant_count=[]
        max_vowel=0
        max_consonant=0
        for ch in s:
            if ch in ['a','e','i','o','u']:
                vowel.append(ch)
            else:
                consonant.append(ch) 

        for i in vowel:
            vowels_count.append(vowel.count(i))

        for j in consonant:
            consonant_count.append(consonant.count(j))

        
        for i in vowels_count:
            if max_vowel<i:
                max_vowel=i

        for j in consonant_count:
            if max_consonant<j:
                max_consonant=j

        return max_vowel + max_consonant                


        