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

if __name__ == '__main__':
    print(checkSubsequenceSum([4, 3, 9, 2] , k = 10))