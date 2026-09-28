class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        count=0
        maximum=0
        for ch in s:
            if ch=="(":
                count+=1
                if count>maximum:
                    maximum=count

                #stack.append(ch)
            elif count>=1 and ch==")":
                count-=1 
        return maximum           

        