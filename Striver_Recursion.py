# Generate all binary strings without consecutive ones
def generate(n):
    result = [] # To count the results fibonacci series is the optimised solution
    def helper(n, curr, result):
        if len(curr) == n:
            result.append(curr)
            return
        
        helper(n, curr + '0', result)

        if not curr or curr[-1] == '0':
            helper(n, curr + '1', result)

    helper(n, '', result)
    return result

# Power Set
def powerSet(s):
    result = []
    current = []
    def helper(s, index, current, result):
        if index == len(s):
            result.append(''.join(current))
            return
        
        helper(s, index + 1, current, result)

        current.append(s[index])
        helper(s, index + 1, current, result)

        current.pop()

    helper(s, 0, current, result)
    return result

# Count all subsequence with sum k
def countSubsequenceSum(arr, k):
    def helper(ind, summ, arr):
        if summ == 0:
            return 1
        if ind == len(arr):
            return 0

        return helper(ind + 1, summ - arr[ind], arr) + helper(ind + 1, summ, arr)

    return helper(0, k, arr)

# Check Subsequence with sum k
def checkSubsequenceSum(arr, k):
    def helper(arr, ind, k):
        if k == 0:
            return True
        if k < 0:
            return False
        if ind == len(arr):
            return k == 0

        return helper(arr, ind + 1, k) or helper(arr, ind + 1, k - arr[ind])
    return helper(arr, 0, k)

# Combination Sum
def combinationSums(arr, target):
    res = []
    ds = []
    def helper(arr, target, ind, ds, res):
        if ind == len(arr):
            if target == 0:
                res.append(ds[:])
            return

        if arr[ind] <= target:
            ds.append(arr[ind])
            helper(arr, target - arr[ind], ind, ds, res)

            ds.pop()
        helper(arr, target, ind + 1, ds, res)

    helper(arr, target, 0, ds, res)

    return res

# Combination Sum 2 (No duplicates)
def combinationSums2(arr, target):
    result = []
    curr = []
    arr.sort()
    def helper(arr, target, index, curr, result):
        if target == 0:
            result.append(curr[:])
            return 
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue
            if arr[i] > target:
                break

            curr.append(arr[i])
            helper(arr, target - arr[i], i + 1, curr, result)
            curr.pop()

    helper(arr, target, 0, curr, result)

    return result

# Subsets 1
def subsets1(arr):
    result = []
    def helper(arr, index, summ, result):
        if index == len(arr):
            result.append(summ)
            return

        helper(arr, index + 1, summ, result)
        helper(arr, index + 1, summ + arr[index], result)

    helper(arr, 0, 0, result)

    return result

# Subsets 2
def subsets2(arr):
    curr = []
    result = []
    def helper(arr, index, curr, result):
        result.append(curr[:])
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue

            curr.append(arr[i])
            helper(arr, i + 1, curr, result)
            curr.pop()

    helper(arr, 0, curr, result)

    return result

# Combination 3
def combinationSums3(k, n):
    # k -> target value
    # n -> limit of numbers

    arr = [i for i in range(1, 10)]
    result = []
    curr = []

    def helper(arr, k, n, ind, curr, result):
        if n == 0:
            if k == 0:
                result.append(curr[:])
            return 
        for i in range(ind, len(arr)):
            if arr[i] > k:
                break
            curr.append(arr[i])
            helper(arr, k - arr[i], n - 1, i + 1, curr, result)
            curr.pop()

    helper(arr, k, n, 0, curr, result)
    return result

# Letter Combination of a phone number
def letterCombinations(digits):
    result = []
    curr = []
    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def helper(index):
        if index == len(digits):
            result.append(''.join(curr))
            return

        current_digit = digits[index]
        possible_letters = d[current_digit]

        for i in possible_letters:
            curr.append(i)
            helper(index + 1)
            curr.pop()

    helper(0)
    return result
    
# Word Search
def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    def dfs(i, j ,idx):
        if idx == len(word):
            return True

        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[idx]:
            return False

        temp = board[i][j]
        board[i][j] = '#'

        found = (
            dfs(i + 1, j, idx + 1) or
            dfs(i - 1, j, idx + 1) or
            dfs(i, j - 1, idx + 1) or
            dfs(i, j + 1, idx + 1)
        )

        board[i][j] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False

def solveQueens(n):
    def solve(col, board, n, leftRow, upperDiagonal, lowerDiagonal, ans):
        if col == n:
            ans.append(["".join(row)for row in board])
            return

        for row in range(n):
            if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:

                board[row][col] = 'Q'
                leftRow[row] = lowerDiagonal[row + col] = upperDiagonal[n - 1 + col - row] = 1

                solve(col + 1, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)

                board[row][col] = '.'
                leftRow[row] = lowerDiagonal[row + col] = upperDiagonal[n - 1 + col - row] = 0

    ans = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    leftRow = [0] * n
    upperDiagonal = [0] * (2 * n - 1)
    lowerDiagonal = [0] * (2 * n - 1)
    solve(0, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)
    return ans

if __name__ == '__main__':
    print(solveQueens(4))