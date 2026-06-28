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


if __name__ == "__main__":
    mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(f'The Target is in matrix: {search2D2(mat, 11)}')