class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        prefix=""
        new=""
        rev=""
        for i in word:
            if i!=ch:
                prefix+=i
            else:
                prefix+=i
                break

        rev=prefix[::-1]
        new+=rev+word[len(prefix):]
        return new        


        