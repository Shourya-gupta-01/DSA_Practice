# Generate all binary strings without consecutive ones
def generate(n):
    result = []
    def helper(n, curr, result):
        if len(curr) == n:
            result.append(curr)
            return
        
        helper(n, curr + '0', result)

        if not curr or curr[-1] == '0':
            helper(n, curr + '1', result)

    helper(n, '', result)
    return result

if __name__ == '__main__':
    print(generate(3))