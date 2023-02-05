# util function : swap i and j ele of arr 
def swap (i, j, arr):
    tmp=arr[i]
    arr[i]=arr[j]
    arr[j]=tmp

# bubble sort function def 
# complexity O(n^2) Auxiliary Space: O(1)
def bubble_sort(arr):
    n = len(arr)
    loop_cnt=0
    for i in range(0,n):
        for j in range(0,n-i-1):
            loop_cnt+=1
            if arr[j] > arr[j+1] :
                swap(j,j+1,arr) # util function
    return loop_cnt

# bubble sort function def 
# complexity O(n^2) Auxiliary Space: O(1)
def bubble_sort_optimized(arr):
    n = len(arr)
    loop_cnt=0
    for i in range(0,n):
        swap_ind=False  # swapped indicator 
        for j in range(0,n-i-1):
            loop_cnt+=1
            if arr[j] > arr[j+1] :
                swap(j,j+1,arr) # util function
                swap_ind=True
        if not swap_ind : # if no elements are getting swapped, break out of the i loop 
            break
    return loop_cnt



# main 
if __name__ == "__main__":
    arr=[51, 2, 4, 7, 100, 30, 1,67 ,1 ,1, 76,1, 33,343434,34, 455,676,676,98,8976,4,33,34,2,4,0,76,10,5,44,3,3,22,2,2,56]
    arr2=[51, 2, 4, 7, 100, 30, 1,67 ,1 ,1, 76,1, 33,343434,34, 455,676,676,98,8976,4,33,34,2,4,0,76,10,5,44,3,3,22,2,2,56]
    print("In Main()\nunsorted arr :")
    print(arr)
    cnt=bubble_sort(arr)
    print(f"sorted arr cnt :{cnt}")
    print(arr)
    cnt=bubble_sort_optimized(arr2)
    print(f"sorted arr cnt :{cnt}")
    print(arr2)