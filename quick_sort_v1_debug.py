#quick sort 

#util function to swap i , j ele of gievn arr
def swap(arr, i , j ) : 
    arr[i], arr[j] = arr[j] , arr[i]

#partitioning function for selecting pivot, sorting and returning the index of pivot 
def partition_array(arr , low , high):
    pivot = arr [low]
    i = high

    print(f"1.i:{i}, pivot:{pivot}, arr:{arr}")
    for j in range (high, low, -1):
        print(f"for.i:{i}, j:{j}")
        if (arr[j] >= pivot) :
            print(f"before swap.i:{i}, j:{j}, arr:{arr}")
            swap(arr, i, j )
            i-=1
            print(f"swapped.i:{i}, j:{j}, arr:{arr}")

    print(f"2.i:{i}, pivot:{pivot}, arr:{arr}")
    swap(arr, i, low)
    print(f"3.i:{i}, pivot:{pivot}, arr:{arr}")
    return i



#quick sort 
#version 1 : select 1st element as pivot
def quick_sort(arr , low , high):
    print(f"arr:{arr}\nlow:{low}, high:{high}")
    if (low < high):
        pivot = partition_array(arr, low , high)
        quick_sort(arr, low , pivot - 1)
        quick_sort(arr, pivot + 1 , high)
    else :
        print(f"#Exited  >> low:{low}, high:{high}")


#main 
if __name__ == "__main__" :
    arr=[10, 2, 15, 17, 8, 9]
    print(f"Input arr : {arr}")
    quick_sort(arr, 0, len(arr)-1)
    print(f"Sorted arr : {arr}")

