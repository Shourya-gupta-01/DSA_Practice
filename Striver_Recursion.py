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

if __name__ == '__main__':
    print(subsets1([5, 2, 1]))