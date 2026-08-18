#For Recursive Approach : T.C. - O(N) and S.C. - O(N)
def Powerfun(x,n): #Recursive appproach only  
    if(n==0):
        return 1
    else:
        return n*Powerfun(x,n-1)

result=Powerfun(2,5)   
print(result) 


def Powerfun_v1(x,n):   # For Divide And Conquer version 1  T.C - O(N)  , S.C - O(N)
    
    if(n==0):  #base case 
        return 1
    
    elif(n % 2==0):
        return Powerfun_optimized(x,n//2) * Powerfun_optimized(x,n//2)

    else:
        return x * Powerfun_optimized(x,n//2) * Powerfun_optimized(x,n//2)

print(Powerfun_v1(2,7)) 

def Powerfun_optimized(x,n):   #For Divide and Conquer version 2 (optimized) T.C. - O(log n), S.C - O(N)
    
    if(n==0):  #base case 
        return 1

    temp=Powerfun_optimized(x,n//2)  #because we were calling the powerfun 2 times but the value was same so we take a temp variable and assigned the value of Powerfun(x,n//2) to it so now we call the function one time only 
    if(n % 2==0):
        return temp * temp

    else:
        return x * temp * temp

print(Powerfun_optimized(2,7)) 