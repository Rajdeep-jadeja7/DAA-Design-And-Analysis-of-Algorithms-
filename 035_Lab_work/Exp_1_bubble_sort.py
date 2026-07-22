def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1):
            if(arr[j]>arr[j+1]):
                (arr[j],arr[j+1])=(arr[j+1],arr[j])

        

arr=[5,1,6,8,2,9,0,2,6]    
bubble_sort(arr)
print(arr) 
