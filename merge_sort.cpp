#include<iostream>
#include "global_types.h"
#include <limits.h>

using namespace std;

int nums[] = { 51, 2, 4, 7, 100, 30, 1,67 ,1 ,1, 76,1, 33,343434,34, 455,676,676,98,8976,4,33,34,2,4,0,76,10,5,44,3,3,22,2,2,56};
// int size = sizeof(arr)/sizeof(arr[0]);
// int nums[] = { };

void merge(int * arr , int start, int mid, int end){

    int l_ln = ( mid - start ) + 1 ;
    int r_ln = ( end - mid ) ;

    int * left = (int*) malloc((l_ln + 1 ) * sizeof(*arr));
    int * right = (int*) malloc((r_ln + 1 ) * sizeof(*arr));

    left[l_ln] = INT_MAX;
    right[r_ln] = INT_MAX;

    for (int i =0 ; i < l_ln ; i ++ ){
        left[i]=arr[start + i];
    }
    for (int i =0 ; i < r_ln ; i ++ ){
        right[i]=arr[mid + 1 + i];
    }


    int l_curr = 0, r_curr = 0;
    for (int i=start; i < end + 1 ; i++ ){
        if (left[l_curr] <= right[r_curr]){

            arr[i]=left[l_curr];
            l_curr++;
        }
        else {
            arr[i]=right[r_curr];
            r_curr++;
        }
    }
}


void merge_sort(int * arr , int start, int end){

    if (start >= end ) 
        return ;
    int mid = (start + end ) / 2 ;
    merge_sort(arr, start, mid);
    merge_sort(arr, mid + 1, end);
    merge(arr, start, mid, end);
}

int main(){
    int ln= (nums[0]==NULL ? 0 : sizeof(nums)/sizeof(nums[0]) );
    cout << "ln : " << ln << "\n" ;

    merge_sort(nums,0,ln-1);
    cout << "Sorted nums: " ;
    for (int i =0 ; i < ln ; i++){
        cout << nums[i] << ", ";
    }
    cout << "\n" ;

    return 0;

}
