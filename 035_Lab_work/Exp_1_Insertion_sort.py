#Insertion Sort - T.C. - O(n^2) and S.C. - O(1)
# Best Case - O(n) : when the array is already sorted
# Average Case - O(n^2) : when elements are randomly placed
# Worst Case - O(n^2): When the array is reverse sorted or in descending order

def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1

        while(j>=0 and arr[j]>key):    #the compiler compiles from left to right so we should write j>=0 first so if it is false then compiler would not check second condition
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arr=[5,1,6,8,2,9,0,2,6]            
insertionsort(arr)
print(arr)      




