class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        preflen=len(pref)
        count=0
        for i in words:
            if i[:preflen]==pref:
                count+=1
        return count        
        