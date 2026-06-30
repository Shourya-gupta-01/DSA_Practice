# Remove Outermost Parenthesis
def removeOuterParenthesis(s):
    start = 0
    cnt = 0
    ans = ''
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            ans += s[start + 1:i]
            start = i + 1
    return ans

# Reverse word in the string (NO O(1) space solution possible)
def reverseWords(s):
    return ' '.join(reversed(s.split()))

if __name__ == '__main__':
    s = '  hello world  '
    print(f'after reversing the string s: {reverseWords(s)}')