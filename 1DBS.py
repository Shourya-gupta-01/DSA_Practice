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

if __name__ == '__main__':
    arr = [3, 4, 6, 7, 9, 12, 16, 17]
    print(f'The x element in at index: {searchX(arr, 1)}')