# Search X in sorted array
def searchX(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return 'Not Found'

# Lower Bound
def lowerBound(arr, x):
    ans = len(arr)
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= x:
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1
    return ans

# Upper Bound
def upperBound(arr, x):
    ans = len(arr)
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > x:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

# Search Insert Position
def searchInsertX(arr, x):
    ans = len(arr)
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= x:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

# Floor and Ceil in Sorted array
def floor_ceil(arr, x):
    floor = -1
    ceil = -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return [arr[mid]] * 2
        if arr[mid] > x:
            ceil = mid
            right = mid - 1
        else:
            floor = mid
            left = mid + 1
    return [arr[floor], arr[ceil]] 

# First and last occurrence
def searchRange(nums, target):
    ans = [-1, -1]
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            ans[0] = mid
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            ans[1] = mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return ans

if __name__ == '__main__':
    arr = [3,5,8,9,15,19]
    print(f'The first and last occurrence of x is at index: {searchRange(arr, 8)}')