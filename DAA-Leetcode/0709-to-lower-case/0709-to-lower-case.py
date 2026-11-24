class Solution:
    def toLowerCase(self, s: str) -> str:
        lower=""
        order=0
        for i in s:
            order=ord(i)
            if order>=65 and order<=90:
                lower+=(chr(order+32))
            else:
                lower+=i
        return lower            
        