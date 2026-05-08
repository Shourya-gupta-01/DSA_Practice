from Sorting_algo import quick_sort

# Find the largest element in the array
def largest_element(arr):
    if len(arr) <= 0:
        return "The size of array is not appropriate"
    maxx = float('-inf')
    for i in arr:
        maxx = max(i, maxx)
    return maxx

# Find the second largest element in the array
def second_largest_element(arr):
    if len(arr) <= 1:
        return "The size of array is not appropriate"
    maxx = float('-inf')
    for i in arr:
        if i > maxx:
            sec_maxx = maxx
            maxx = i
    return sec_maxx

# Find the second smallest element in the array
def second_smallest_element(arr):
    if len(arr) <= 1:
        return "The size of array is not appropriate"
    minn = float('inf')
    for i in arr:
        if i < minn:
            sec_minn = minn
            minn = i
    return sec_minn

# Check if the array is sorted
def is_sorted(arr):
    asc = 0
    dsc = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            asc += 1
        if arr[i] < arr[i + 1]:
            dsc += 1
    return asc == 0 or dsc == 0 

# Remove duplicates from sorted array
def remove_duplicates(arr):
    res = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[res] = arr[i]
            res += 1
    arr[:] = arr[:res] 

# Rotate the array
def rotate(arr, k):
    k = k % len(arr)
    def reverse(arr, low, high):
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    reverse(arr, 0, len(arr) - 1)
    reverse(arr, k, len(arr) - 1)
    reverse(arr, 0, k - 1)

# Move 0's to end
def move_0_end(arr):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[fast], arr[slow] = arr[slow], arr[fast]
        
            slow += 1

if __name__ == '__main__':
    arr = [1, 0, 5, 0, 65, 0, 0, 98, 76, 43]
    # print(f'The Largest element in the array is : {largest_element(arr)}')
    # print(f'The Second Largest element in the array is : {second_largest_element(arr)}')
    # print(f'The Second Smallest element in the array is : {second_smallest_element(arr)}')
    # print(f'The array is sorted : {is_sorted(arr)}')
    # quick_sort(arr)
    # print(f"The sorted array is : {arr}")
    # remove_duplicates(arr)
    # print(f'The array with remove duplicates : {arr}')
    # rotate(arr, k = 3)
    # print(f"The Rotated array by k elements : {arr}")
    move_0_end(arr)
    print(f'The array where 0 are in end : {arr}')