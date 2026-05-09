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

# Linear Search
def linear_search(arr, find):
    for i in range(len(arr)):
        if arr[i] == find:
            return i
    return 'Not Found'

# Union of Two Sorted Arrays
def union_of_two_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    res = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            val = arr1[i]
            i += 1
        else:
            val = arr2[j]
            j += 1
        
        if not res or res[-1] != val:
            res.append(val)

    while i < len(arr1):
        if res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1

    while j < len(arr2):
        if res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1
        
    return res

# Find Missing Number
def missing_num(arr):
    n = len(arr) + 1
    arr_sum = 0
    summ = n * ((n + 1) / 2)

    for i in range(len(arr)):
        arr_sum += arr[i]

    return summ - arr_sum


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
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
    # move_0_end(arr)
    # print(f'The array where 0 are in end : {arr}')
    # print(f'5 is located at : {linear_search(arr, 4)}')
    # print(f'The union of two arrays is : {union_of_two_sorted_arrays(arr1, arr2)}')
    print(f'The Missing number in the array is : {missing_num(arr)}')