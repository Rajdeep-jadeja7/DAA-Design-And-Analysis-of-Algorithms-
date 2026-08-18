# Merge Sort - T.C. - O(n logn) and S.C. - O(n)
# Best Case - O(nlogn) : when the array is already sorted but still merge sort divides the array and merges the elements.
# Average Case - O(nlogn) : when elements are randomly placed.
# Worst Case - O(nlogn): When the array is reverse sorted or in descending order
# In every arrangement of the elements of array the divide and merge process remains the same .
# SPace Complexity = O(n) because we created new array to store the merge part.


def merging(A,B):                    #This is the conquer part of the merge sort
    merge=[0]*(len(A)+len(B))        #to create a new output array of size of A+B and assigning the value of all elements as 0
    i,j,k=0,0,0

    while(i<len(A) and j<len(B)):
        if(A[i]<B[j]):
            merge[k]=A[i]
            k+=1
            i+=1
        else:
            merge[k]=B[j]
            k+=1
            j+=1
    while(i<len(A)):
        merge[k]=A[i]
        k+=1
        i+=1

    while(j<len(B)):
        merge[k]=B[j]
        j+=1
        k+=1
    return merge        


def divide(arr):    #This is the divide part of the Merge sort 
    if(len(arr)<=1):
        return arr

    mid=len(arr)//2

    left=divide(arr[:mid])
    right=divide(arr[mid:])

    return merging(left,right)

arr=[1,6,4,3,5,9,5]
print(divide(arr))