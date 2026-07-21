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

if __name__ == '__main__':
    print(powerSet('abc'))