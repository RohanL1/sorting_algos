#include<iostream>
#include "global_types.h"
#include <limits.h>


using namespace std;


int nums[]= {1, 34 , -10, -40, -2, 10, 9, 10, -7, 10, -5} ;

struct subArr{
    int low;
    int high;
    long sum ; 
} ;

void setVal(subArr &arr, int low, int high, long sum){

}

subArr findMaxCorssSubArr(int * nums, int l, int h){
    subArr MaxSub;
    MaxSub.low=0;
    MaxSub.high=0;
    MaxSub.sum=0;
    return MaxSub;
}


subArr findMaxSubArr(int * nums, int l, int h,subArr &MaxSub){
    subArr MaxSub;
    if (h==l){
        setVal(MaxSub,l,l,nums[l]);
        return MaxSub;
    }
}



int main(){
    int ln= (nums[0]==NULL ? 0 : sizeof(nums)/sizeof(nums[0]) );
    subArr MaxSub;
    findMaxSubArr(nums,0,ln,MaxSub);

    return 0;
}