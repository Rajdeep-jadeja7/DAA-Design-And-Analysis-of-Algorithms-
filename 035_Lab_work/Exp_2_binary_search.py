# For Binary Search THe array must be sorted .
# Binary Search   T.C. - O(logn)  and  S.C. - O(1)
# Best Case T.C. - O(1) : when the target element is at middle element so on first comparison we will find it.
# Average Case T.C. - O(logn)  : when target element is found after some comparisons. 
# Worst case - T.C. - O(logn)  when the target element is at last position or when Target element is not present in the array.
# Each step cuts the search space approximately in half
# Even in the worst case, we keep cutting the search space in half until either we find the element or there is nothing left to search.

def binary_search(arr,low,high,target):
    mid=(low+high)//2
    if(low>high):
        return -1
    if (target==arr[mid]):
        return mid
                                        
    elif(target>arr[mid]):
        #low=mid+1
        return binary_search(arr,mid+1,high,target)

    #elif(target<arr[mid]):
    else:
        #high=mid-1 
        return binary_search(arr,low,mid-1,target)
    
arr=[1,2,3,4,5,6,7]   #THe array should be sorted 
target=6
result=binary_search(arr,0,len(arr)-1,target)   

if(result==-1):
    print("Element not found")
else:
    print("Element found at index:",result)    

        