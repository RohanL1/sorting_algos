#quick sort 
# V1 taking 1st ele of arr as pivot

#util function to swap i , j ele of gievn arr
def swap(arr, i , j ) : 
    arr[i], arr[j] = arr[j] , arr[i]

#partitioning function 
#for selecting pivot, sorting and returning the index of pivot 
def partition_array(arr , low , high):
    pivot = arr [low] # pick 1st ele as pivot
    i = high 

    # loop from high to low : check for ele greater then pivot if greater swap with i
    for j in range (high, low, -1):
        if (arr[j] >= pivot) :
            swap(arr, i, j )
            i-=1

    swap(arr, i, low) # insert pivot at its correct position by swapping with i

    return i # retun index of pivot



#quick sort function
#version 1 : select 1st element as pivot
def quick_sort(arr , low , high):
    if (low < high): # exit condition of recurrsion
        pivot = partition_array(arr, low , high) # partition arr
        quick_sort(arr, low , pivot - 1) # quick sort left part of arr
        quick_sort(arr, pivot + 1 , high) # quick sort right part of arr


#main 
if __name__ == "__main__" :
    arr=[10, 2, 15, 17, 8, 9]
    print(f"Input arr : {arr}")
    quick_sort(arr, 0, len(arr)-1)
    print(f"Sorted arr : {arr}")

