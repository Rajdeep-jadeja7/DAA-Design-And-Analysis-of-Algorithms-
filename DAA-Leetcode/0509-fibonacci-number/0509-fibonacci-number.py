class Solution:
    def fib(self, n: int) -> int:
        if n<=0:
            return 0
        elif n==1 or n==2:
            return 1    

        first=1
        second=1
        third=0
        for _ in range(2,n):
            third=first+second
            first,second=second,third
        return third    

        
    