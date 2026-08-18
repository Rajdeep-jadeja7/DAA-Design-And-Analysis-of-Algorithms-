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

        