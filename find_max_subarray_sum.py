nums = [1, 34 , -10, -40, -2, 10, 9, 10, -7, 10, -5, 100, 20, -10, 0, -150, -1, 10, -12, 12, 19]

def findMaxCrossSubArr(arr, low, mid, high) :
    
    maxLeft=mid
    maxRight=mid
    
    leftSum = float('-inf')
    sum=0
    for i in range(mid, low-1, -1 ) : 
        sum = sum + arr[i]
        if sum > leftSum : 
            maxLeft=i
            leftSum=sum

    rightSum = float('-inf')
    sum=0
    for i in range(mid+1, high+1, 1 ) : 
        sum = sum + arr[i]
        if sum > rightSum : 
            maxRight=i
            rightSum=sum

    return (maxLeft,maxRight,leftSum+rightSum) 

def findMaxSubArr(arr, low, high) :
    
    if low == high : 
        return (low,low,arr[low])
    else :
        mid = ( low + high ) // 2
        leftLow, leftHigh, leftSum = findMaxSubArr(arr, low, mid)
        rightLow, rightHigh, rightSum = findMaxSubArr(arr, mid+1, high)
        crossLow, crossHigh, crossSum = findMaxCrossSubArr(arr, low, mid, high)

        if leftSum >= rightSum and leftSum >=crossSum :
            return (leftLow, leftHigh, leftSum)
        elif rightSum > leftSum and rightSum > crossSum : 
            return (rightLow, rightHigh, rightSum)
        else : 
            return (crossLow, crossHigh, crossSum)


def main():
    print("In main\nINPUT  : {} \nOUTPUT : {}".format(nums, findMaxSubArr(nums,0,len(nums)-1) ))
    return 0

if __name__ == "__main__":
    main()