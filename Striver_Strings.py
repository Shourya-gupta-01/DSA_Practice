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

# Largest Odd number in a string
def largestOddNumber(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if num[i] in "13579":
            return num[:i + 1]
    return ""

# Longest Common Prefix
def longestCommonPrefix(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if len(s) == i or s[i] != strs[0][i]:
                return res            
        res += strs[0][i]
    return res

# Isomorphic string
def isIsomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# Rotate string
def rotateString(s, goal):
    return len(s) == len(goal) and goal in (s + s)

# Check Anagram
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    ds = {}
    dt = {}
    for i in range(len(s)):
        if s[i] in ds:
            ds[s[i]] += 1
        else:
            ds[s[i]] = 1

        if t[i] in dt:
            dt[t[i]] += 1
        else:                
            dt[t[i]] = 1
    return ds == dt

# Sort Characters by Frequency
def frequencySort(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = ''
    for i, j in sorted(d.items(), key = lambda item: item[1], reverse = True):
        ans += i * j

    return ans

# Maximum Nesting Depth of Parenthesis
def maxDepth(s: str) -> int:
    stk = []
    res = 0
    for i in s:
        if i == '(':
            stk.append('(')
            res = max(res, len(stk))
        if i == ")":
            stk.pop()
    return res

if __name__ == '__main__':
    s = '(1+(2*3)+((8)/4))+1'
    print(f'Max Depth: {maxDepth(s)}')