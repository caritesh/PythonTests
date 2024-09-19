#Data Structures
#Finding a peak

# Find the peak element in the array > recursive binary search
def findPeakUtil(arr, low, high, n):

    # Find index of middle element
    # low + (high - low) / 2
    mid = low + (high - low)/2
    mid = int(mid)

    #compare mid elements with its neighbors
    if ((mid == 0) or arr[mid-1] <= arr[mid] and
        (mid == n-1) or arr[mid+1] <= arr[mid]):
        return mid
    
    #if mid element is not peak
    elif(mid > 0 and arr[mid-1]>arr[mid]):
        return findPeakUtil(arr,low,mid-1,n)
    else:
        return findPeakUtil(arr,mid+1,high,n)

def findPeak(arr,n):
    return findPeakUtil(arr,0,n-1,n)

arr = [1, 3, 20, 4,21, 0]
n = len(arr)
n
findPeak(arr,n)

