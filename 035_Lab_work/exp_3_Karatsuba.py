# Karatsuba  T.C. - O(n^1.52)
# For the same Multiplication Iterative approach and Divide And conquer approach both take T.C. - O(n^2)

def Karatsuba(x,y):
    if (len(x)<=1 or len(y)<=1):
        return x * y

    p=len(x)
    q=len(y)
    n=max(p,q)

    B=(x % (10 ** (n//2)))
    A=(x // (10 ** (n//2)))
    C=(y //(10 ** (n//2)))
    D=(y % (10 ** (n//2)))

    ac = Karatsuba(A,C)
    bd= Karatsuba(B,D)
    abcd = Karatsuba((A+B),(C+D))-ac-bd

    return ((ac * 10 **n) + bd +(abcd * 10 ** (n//2)))

X=1234
Y=5678
Karatsuba(X,Y)

