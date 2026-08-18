# Merging two Sorted arrays : T.C. - O(n+m) where n is length of array A and m is the lenth of array B
# But if both the arrays have same size then T.C. - O(n+n) = O(2n) = O(n)

a=[1,3,5,7,9,11,16,18]
b=[2,4,6,8,10,12]

def merging_two_sorted_arrays(A,B):
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

print(merging_two_sorted_arrays(a,b))
