# Linear Search   T.C. - O(n)    S.C. - O(1)
# Best Case T.C. - O(1) : when the target element is at first position
# Average Case T.C. - O(n)  When target is somewhere in the middle on average.
# Worst case - T.C. - O(n) when the target element is at the Last position or when Target Don't exxist because then we have to check all the n elements.



def linearsearch(arr,target):
    for i in range(0,len(arr)):
        if (arr[i]==target):
            return i
    return -1 
    
arr=[1,2,3,4,5,6]
result=linearsearch(arr,4)

if(result==-1):
    print("Element not  found inside the list ")
else:
    print("Element found in the list at index:",result)    