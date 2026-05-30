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

if __name__ == '__main__':
    arr = [3,5,8,15,19]
    print(f'The x element in at index: {lowerBound(arr, 9)}')