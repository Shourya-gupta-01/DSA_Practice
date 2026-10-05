# Maximum points you can obtain from cards 
def maxScore(cardPoints: list[int], k: int) -> int:
    ans = sum(cardPoints[:k])
    curr_sum = ans
    temp = k
    cnt = 0

    while cnt < k:
        cnt += 1
        curr_sum += cardPoints[len(cardPoints) - cnt]
        curr_sum -= cardPoints[temp - 1]
        temp -= 1
        ans = max(curr_sum, ans)
        
    return ans

# Longest Substring without repeating Character
def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    reslen = 0
    l = 0
    r = 0

    while l < len(s) and r < len(s):
        if d.get(s[r], 0) == 1:
            d[s[l]] = 0
            l += 1
        else:
            d[s[r]] = 1
            reslen = max(reslen, (r - l + 1))
            r += 1

    return reslen

# Max Consecutives ones III
def longestOnes(nums: list[int], k: int) -> int:
    l = 0
    zeroes = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            zeroes += 1
        if zeroes > k:
            if nums[l] == 0:
                zeroes -= 1
            l += 1

    return len(nums) - l

# Fruit into Baskets
def totalFruit(fruits: list[int]) -> int:
    d = {}
    l = 0

    for r in range(len(fruits)):
        d[fruits[r]] = d.get(fruits[r], 0) + 1
        if len(d) > 2:
            d[fruits[l]] -= 1
            if d[fruits[l]] == 0:
                del d[fruits[l]]
            l += 1

    return len(fruits) - l

# Longest Substring with k uniques
def longestKSubStr(s: str, k: int) -> int:
    d = {}
    l = 0
    res = -1

    for r in range(len(s)):
        d[s[r]] = d.get(s[r], 0) + 1

        if len(d) > k:
            d[s[l]] -= 1
            if d[s[l]] == 0:
                del d[s[l]]
            l += 1
        if len(d) == k:
            res = max(res, r - l + 1)

    return res

if __name__ == '__main__':
    print(longestKSubStr('aaaa', 2))

