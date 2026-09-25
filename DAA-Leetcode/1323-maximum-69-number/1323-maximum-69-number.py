class Solution:
    def maximum69Number (self, num: int) -> int:
        n=str(num)
        for ch in n:
            n=n.replace("6","9",1)
            break

        n=int(n)
        return n    


        