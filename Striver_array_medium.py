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

# Majority element
def majorityElement(arr):
    if not arr: return None
    
    cnt = 0
    element = None
    
    for x in arr:
        if cnt == 0:
            element = x
            cnt = 1
        elif x == element:
            cnt += 1
        else:
            cnt -= 1
            
    return element

# Kadane's Algorithim:
def kadaneAlgo(arr):
    ans = float('-inf')
    ind = [0, 0]
    temp = 0
    start = 0

    for i in range(len(arr)):
        temp += arr[i]
        if ans < temp:
            ans = temp
            ind[1] = i
            ind[0] = start
        if temp < 0:
            temp = 0
            start = i + 1
        
    return ans, ind

# Stock buy and sell
def maxProfit(arr):
    gloabalMin = float('inf')
    localMax = -1
    profit = 0

    for i in arr:
        if i < gloabalMin:
            gloabalMin = i
            localMax = 0
        if i > localMax:
            localMax = i
            profit = max(profit, localMax - gloabalMin)

    return profit

# Rearrange array element by sign
def rearrangeEle(arr):
    res = [0] * len(arr)
    pos_ind = 0
    neg_ind = 1
    for i in arr:
        if i > 0:
            res[pos_ind] = i
            pos_ind += 2
        else:
            res[neg_ind] = i
            neg_ind += 2
    return res

# Next Permutation
def nextPermutation(arr):
    ind = -1
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            ind = i
            break
    if ind == -1:
        arr.reverse()
        return 
    for i in range(len(arr) - 1, ind, -1):
        if arr[ind] < arr[i]:
            arr[ind], arr[i] = arr[i], arr[ind]
            break
    arr[ind + 1:] = reversed(arr[ind + 1:])

# Leader's in an array [Left to right] [Space -> O(n)]
def leaders(arr):
    stk = []
    for i in arr:
        if stk and stk[-1] > i:
            stk.append(i)
        else:
            while stk and stk[-1] < i:
                stk.pop()
            stk.append(i)
    return stk

# [Right to Left] [Space -> O(1)]
def leaders(arr):
    n = len(arr)
    if n == 0:
        return []
    
    res = []
    max_from_right = arr[n-1]
    res.append(max_from_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            res.append(max_from_right)
    
    return res[::-1]

# Longest Consecutive Subsequence in an array
def longestConsecutive(arr):
    longest = 0
    st = set(arr)

    for it in st:
        if it - 1 not in st:
            cnt = 1
            x = it

            while x + 1 in st:
                x = x + 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

# Set Matrix 0's
def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dummy = [1] * m
    zero = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero = 0
                dummy[j] = 0
        if zero == 0:
            matrix[i] = [0] * m
        zero = 1

    for j in range(m):
        if dummy[j] == 0:
            for i in range(n):
                matrix[i][j] = 0

# Rotate matrix by 90
def rotateMatrix90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(i, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in matrix:
        i.reverse()

if __name__ == "__main__":
    arr = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
    # print(f'The target sum exist in arr : {two_sum_exists(arr, 11)}')
    # print(f'The indices of target sum exist in arr : {two_sum_indices(arr, 11)}')
    # print(f'The sorted arr is : {sortZeroOneTwo(arr)}')
    # print(f'The majority element in the array is: {majorityElement(arr)}')
    # print(f'The maximum sum subarray is : {kadaneAlgo(arr)}')
    # print(f'The profit you get : {maxProfit(arr)}')
    # print(f'The array with alternate sign element : {rearrangeEle(arr)}')
    # nextPermutation(arr)
    # print(f'The next permutation for the given input is {arr}')
    # print(f'The Leaders of the array are : {leaders(arr)}')
    # print(f'The Longest Consecutive Subsequence in an array is : {longestConsecutive(arr)}')
    # setZeroes(arr)
    # print(f'Set matrix zeroes : {arr}')
    rotateMatrix90(arr)
    print(f'The matrix is rotated by 90 degree : {arr}')