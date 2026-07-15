def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1

        while(arr[j]>key and j>=0):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arr=[5,1,6,8,2,9,0,2,6]            
insertionsort(arr)
print(arr)      


