
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