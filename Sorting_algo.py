# Selection Sort
def selection_sort(arr):
    if len(arr) == 0:
        return "The Array is empty"
    for i in range(len(arr)):
        minn = arr[i]
        ind = i
        for j in range(i, len(arr)):
            if minn > arr[j]:
                minn = arr[j]
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i]

    return arr

# Bubble Sort
def bubble_sort(arr):
    if len(arr) == 0:
        return "The Array is empty"
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Insertion Sort
def insertion_sort(arr):
    if len(arr) == 0:
        return "The Array is empty"
    for i in range(len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                break

    return arr

# Merge Sort
def merge_sort(arr, low, high):
    if low == high:
        return
    mid = low + (high - low) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

# Helper Func. Merge Sort
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    if left <= mid:
        temp.extend(arr[left:mid + 1])

    if right <= high:
        temp.extend(arr[right:high + 1])

    for i in range(len(temp)):
        arr[low + i] = temp[i]

# Quick Sort
def quick_sort(arr):
    if len(arr) == 0:
        return "The Array is empty"
    
    low = 0
    high = len(arr) - 1

    def helper(arr, low, high):
        if low >= high:
            return
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        
        helper(arr, low, j - 1)
        helper(arr, j + 1, high)
    helper(arr, low, high)

# Recursive Bubble Sort
def rec_bubble_sort(arr):
    def helper(arr, n):
        if n == 0:
            return
        
        swapped = False
        
        for j in range(n):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            return
        
        helper(arr, n - 1)
    helper(arr, len(arr) - 1)

# Recursive Insertion Sort
def rec_insertion_sort(arr):    # My Approach --> right - left and uses swap and shift
    def helper(arr, n):
        if n < 0:
            return
        for i in range(n, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                break
        helper(arr, n - 1)
    helper(arr, len(arr) - 1)

if __name__ == "__main__":
    l = [40, 60, 7, 80, 43, 68, 98, 54]

    # print(f'Using Selection Sort : {selection_sort(l)}')
    # print(f'Using Bubble Sort : {bubble_sort(l)}')
    # print(f'Using Insertion Sort : {insertion_sort(l)}')
    # merge_sort(l, 0, len(l) - 1)
    # print(f'Using Merge Sort : {l}')
    # quick_sort(l)
    # print(f'Using Quick Sort : {l}')
    # rec_bubble_sort(l)
    # print(f'Using recursive Bubble Sort : {l}')
    rec_insertion_sort(l)
    print(f'Using recursive Insertion Sort : {l}')