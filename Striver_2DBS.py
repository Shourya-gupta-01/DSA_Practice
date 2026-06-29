# Find the row with maximum number of 1's
def rowWithMax1s(arr):
    n = len(arr)
    ans = [-1, 0]
    for i in range(n):
        low = 0
        high = n - 1
            
        while low <= high:
            mid = low + (high - low) // 2
                
            if arr[i][mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
                    
        if ans[-1] < n - low:
            ans[:] = [i, n - low]
                
    return ans[0]

# Search in a 2D matrix Row and Column Sorted:
def search2D1(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    pointer = m - 1
    for i in range(n):
        while pointer >= 0 and pointer < m:
            if matrix[i][pointer] == target:
                return True
            elif matrix[i][pointer] > target:
                pointer -= 1
            else:
                break
    return False

# Search in 2D Matrix 
def search2D2(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    for i in matrix:
        if target > i[-1]:
            continue
        else:
            low = 0
            high = m - 1

            while low <= high:
                mid = low + (high - low) // 2
                if i[mid] == target:
                    return True
                if i[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
    return False

# Find Peak Element in a 2D matrix
def findPeakGrid(matrix):

    def findMax(matrix, col):
        maxx = float('-inf')
        index = -1
        for i in range(len(matrix)):
            if matrix[i][col] > maxx:
                maxx = matrix[i][col]
                index = i
        return index
    
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = m - 1

    while low <= high:
        mid = low + (high - low) // 2
        row = findMax(matrix, mid)

        left = matrix[row][mid - 1] if mid - 1 >= 0 else float('-inf')
        right = matrix[row][mid + 1] if mid + 1 < m else float('-inf')

        if matrix[row][mid] > left and matrix[row][mid] > right:
            return [row, mid]
        elif left > matrix[row][mid]:
            high = mid - 1
        else:
            low = mid + 1

    return [-1, -1]

# Find median of the 2D matrix
def medianMatrix(matrix):

    def helper(matrix, x, n, m):
        cnt = 0
        for i in range(n):
            low = 0
            high = m - 1

            while low <= high:
                mid = low + (high - low) // 2
                if matrix[i][mid] <= x:
                    low = mid + 1
                else:
                    high = mid - 1
            cnt += low

        return cnt
        
    n = len(matrix)
    m = len(matrix[0])
    req = (n * m) / 2

    low = float('inf')
    high = float('-inf')

    for i in range(n):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][m - 1])

    while low <= high:
        mid = low + (high - low) // 2
        smallcnt = helper(matrix, mid, n, m)
        if smallcnt <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low

if __name__ == "__main__":
    mat = [
        [1, 3, 8],
        [2, 3, 4],
        [1, 2, 5],
        ]
    print(f'The median of the matrix: {medianMatrix(mat)}')