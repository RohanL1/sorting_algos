#include<iostream>
#include "global_types.h"
#include <limits.h>

using namespace std;

int nums[] = { 51, 2, 4, 7, 100, 30};
int ln=6;

void merge(int * arr , int start, int mid, int end){

    cout << "MERGE(start : " << start << ", mid : " << mid << ", end : " << end << ")\n";
    int l_ln = ( mid - start ) + 1 ;
    int r_ln = ( end - mid ) ;

    int * left = (int*) malloc((l_ln + 1 ) * sizeof(*arr));
    int * right = (int*) malloc((r_ln + 1 ) * sizeof(*arr));

    left[l_ln] = INT_MAX;
    right[r_ln] = INT_MAX;

    for (int i =0 ; i < l_ln ; i ++ ){
        left[i]=arr[start + i];
    }

    cout << "intial left : ";
    for (int i =0 ; i < l_ln +1 ; i ++ ){
        cout << left[i] << ", ";
    }
    cout << "\n";
    for (int i =0 ; i < r_ln ; i ++ ){
        right[i]=arr[mid + 1 + i];
    }

    cout << "intial right : ";
    for (int i =0 ; i < r_ln +1 ; i ++ ){
        cout << right[i] << ", ";
    }
    cout << "\n";

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

    cout << "Final merged : ";
    for (int i=start; i < end + 1 ; i++ ){
        cout << arr[i] << ", ";
    }
    cout << "\nMERGE END.\n";
}


void merge_sort(int * arr , int start, int end){

    if (start >= end ) 
        return ;
    int mid = (start + end ) / 2 ;
    cout << "mid:" << mid << "\n";
    merge_sort(arr, start, mid);
    cout << "left Sorted nums: \n" ;
    for (int i =start ; i < mid +1 ; i++){
        cout << arr[i] << ", ";
    }
    cout << "\n" ;
    merge_sort(arr, mid + 1, end);
    cout << "right Sorted nums: \n" ;
    for (int i =mid + 1 ; i < end +1 ; i++){
        cout << arr[i] << ", ";
    }
    cout << "\n" ;
    merge(arr, start, mid, end);
    cout << "MERGED nums: \n" ;
    for (int i =start; i < end +1 ; i++){
        cout << arr[i] << ", ";
    }
    cout << "\n" ;
    cout << "mid : " << mid << " END.\n" ;
}

int main(){

    cout << "In main\ncalling merge_sort() for input : \n" ;
    for (int i =0 ; i < ln ; i++){
        cout << nums[i] << ", ";
    }
    cout << "\n" ;
    merge_sort(nums,0,ln-1);
    
    cout << "Sorted nums: \n" ;
    for (int i =0 ; i < ln ; i++){
        cout << nums[i] << ", ";
    }
    cout << "\n" ;
    return 0;

}
