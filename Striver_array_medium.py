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

if __name__ == "__main__":
    arr = [2, 6, 11, 5, 8]
    print(f'The target sum exist in arr : {two_sum_exists(arr, 11)}')
    print(f'The indices of target sum exist in arr : {two_sum_indices(arr, 11)}')