# Two sum variant 1
def two_sum_exists(arr, target):
    temp_tup = [(num, ind) for ind, num in enumerate(arr)]
    
    temp_tup.sort(key = lambda x: x[0])

    i = 0
    j = len(arr) - 1
    while i < j:
        temp = temp_tup[i][0] + temp_tup[j][0]
        if temp == target:
            return True
        elif temp > target:
            j -= 1
        else:
            i += 1
    return False

# Two sum variant 2
def two_sum_indices(arr, target):
    temp_tup = [(num, ind) for ind, num in enumerate(arr)]
    
    temp_tup.sort(key = lambda x: x[0])

    i = 0
    j = len(arr) - 1
    while i < j:
        temp = temp_tup[i][0] + temp_tup[j][0]
        if temp == target:
            return sorted([temp_tup[i][1], temp_tup[j][1]])
        elif temp > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]

# Sort 0's, 1's, 2's
def sortZeroOneTwo(arr):
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0

    for i in arr:
        if i == 0:
            cnt_0 += 1
        elif i == 1:
            cnt_1 += 1
        else:
            cnt_2 += 1

    res = cnt_0 * [0] + cnt_1 * [1] + cnt_2 * [2]
    return res

if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0]
    # print(f'The target sum exist in arr : {two_sum_exists(arr, 11)}')
    # print(f'The indices of target sum exist in arr : {two_sum_indices(arr, 11)}')
    print(f'The sorted arr is : {sortZeroOneTwo(arr)}')