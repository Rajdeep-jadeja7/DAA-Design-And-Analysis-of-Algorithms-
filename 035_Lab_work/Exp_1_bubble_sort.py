#Bubble sort T.C. - O(n^2) S.C. - O(1)
# Best Case - O(n) : when the array is already sorted
# Average Case - O(n^2) : when the elements are in Random order 
# Worst Case - O (n^2) : when the array is in Reverse Order then with every Comparison we need to swap.
# Bubble Sort is in-place sorting algorithm so S.C. - O(1)
def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1):
            if(arr[j]>arr[j+1]):
                (arr[j],arr[j+1])=(arr[j+1],arr[j])

        
arr=[5,1,6,8,2,9,0,2,6]    
bubble_sort(arr)
print(arr) 