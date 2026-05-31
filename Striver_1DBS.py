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
def searchRange(nums: list[int], target: int) -> list[int]:
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

# Count occurrences in the sorted array
def countX(arr: list[int], target: int) -> int:
    cnt = searchRange(arr, target)
    if cnt[0] == -1:
        return 0
    return (cnt[1] - cnt[0]) + 1

# Search in rotated sorted array - 1
def searchRotated1(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= arr[left]:
            if target > arr[mid] or target < arr[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < arr[mid] or target > arr[right]:
                right = mid - 1
            else:
                left = mid + 1
    return 'Not Found'

# Search in rotated sorted array - 2
def searchRotated2(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
            continue
        elif arr[mid] >= arr[left]:
            if target > arr[mid] or target < arr[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < arr[mid] or target > arr[right]:
                right = mid - 1
            else:
                left = mid + 1
    return False
    
if __name__ == '__main__':
    arr = [4,5,6,7,1]
    print(f'The element x found at index: {searchRotated2(arr, 2)}')