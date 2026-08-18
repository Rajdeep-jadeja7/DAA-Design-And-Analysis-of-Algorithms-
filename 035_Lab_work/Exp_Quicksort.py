# Quick Sort T.C. - Ω (nlogn)  and S.C. - O(1)
# Best Case: T.C. - O(nlogn) : when the pivot divides the array into 2 equal or nearly equal halves.
# Average : T.C. - O(nlogn) : when the partitions  are balanced 
# but for the worst Case T.C. - O(n^2) when the array is already sorted then quick sort performs worst.

def Partition (arr,Start,end):
    Pindex=Start
    Pivot=arr[end]

    for i in range(Start,end):
        if(arr[i]<=Pivot):
            arr[i],arr[Pindex]=arr[Pindex],arr[i]
            Pindex+=1

    arr[Pindex] , arr[end] = arr[end] , arr[Pindex]
    return Pindex

def quicksort(arr,Start,end):
    if(Start<end):
        Pi=Partition(arr,Start,end)
        quicksort(arr,Start,Pi-1)
        quicksort(arr,Pi+1,end)
    return arr


arr=[4,6,2,3,8,5,9]
result=quicksort(arr,0,len(arr)-1) 
print(result)   

