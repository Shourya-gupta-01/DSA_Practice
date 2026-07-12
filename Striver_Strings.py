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

# Roman to Integer
def romanToInt(s: str) -> int:
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ans = d[s[0]]
    for i in range(1, len(s)):
        if d[s[i]] <= d[s[i - 1]]:
            ans += d[s[i]]
        else:
            ans += d[s[i]] - 2 * d[s[i - 1]] 
    return ans

# String to Integer (atoi)
def myAtoi(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    s = s.strip(" ")
    if not s:
        return 0
    if s[0].isalpha() or s[0] == '.':
        return 0
    ans = "0"
    neg = (s[0] == '-')
    for i in range(len(s)):
        if s[i].isdigit():
            ans += s[i]
        elif i > 0 and not s[i].isdigit():
            num = int(ans) * -1 if neg else int(ans)
            if num >= INT_MIN and num <= INT_MAX:
                return num
            else:
                return INT_MIN if num < INT_MIN else INT_MAX

    num = int(ans) * -1 if neg else int(ans)
    if num >= INT_MIN and num <= INT_MAX:
        return num
    else:
        return INT_MIN if num < INT_MIN else INT_MAX
    
# Count Number of substrings
def count_sustrings(s, k):
    def atMostKDistincts(s, k):
        left = 0 
        res = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            res += (right - left + 1)
        return res

    return atMostKDistincts(s, k) - atMostKDistincts(s, k - 1)

# Longest Palindromic Substring
def longestPalindrome(s):
    res=""
    cnt=0
    for i in range(len(s)):
        l, r=i, i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1>cnt:
                res=s[l:r+1]
                cnt=r-l+1
            l-=1
            r+=1
            
        l, r = i, i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1>cnt:
                res=s[l:r+1]
                cnt=r-l+1
            l-=1
            r+=1
    return res

if __name__ == '__main__':
    s = 'babad'
    print(f'Longest Palindromic substring: {longestPalindrome(s)}')