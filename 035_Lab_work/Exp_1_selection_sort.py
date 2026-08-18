# Selection Sort - T.C. - O(n^2) and S.C. - O(1)
# Best Case - O(n^2) : Even if the array is already sorted then also selection sort searches in the remaining array to find minimum.
# Average Case - O(n^2) : when elements are randomly ordered.
# Worst Case - O(n^2): When the array is reverse sorted or in descending order


def selectionsort(arr):
    n=len(arr)
    for i in range(0,n):
         min_index=i
         for j in range(i,n):
             if(arr[j]<arr[min_index]):
                 min_index=j

         (arr[i],arr[min_index])=(arr[min_index],arr[i])  


arr=[5,1,6,8,2,9,0,2,6]    
selectionsort(arr)
print(arr) 