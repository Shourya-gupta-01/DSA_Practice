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

if __name__ == "__main__":
    arr = [
        [0,0],
        [0,0]
    ]
    print(rowWithMax1s(arr))