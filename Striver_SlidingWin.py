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

# Longest Repeating Character Replacement
def characterReplacement(s: str, k: int) -> int:
    d = {}
    maxFreq = 0
    l = 0

    for r in range(len(s)):
        d[s[r]] = d.get(s[r], 0) + 1
        maxFreq += max(maxFreq, d[s[r]])

        if (r - l + 1) - maxFreq > k:
            d[s[l]] -= 1
            l += 1

    return len(s) - l

# Minimum Window Substring
def minWindow(s: str, t: str) -> str:
    left = 0
    d = {}
    cnt = 0
    minlen = float('inf')
    sIndex = -1

    for i in t:
        d[i] = d.get(i, 0) + 1

    for r in range(len(s)):
        d[s[r]] = d.get(s[r], 0) - 1

        if d[s[r]] >= 0:
            cnt += 1

        while cnt == len(t):
            if r - left + 1 < minlen:
                minlen = r - left + 1
                sIndex = left

            d[s[left]] += 1

            if d[s[left]] > 0:
                cnt -= 1

            left += 1

    if minlen == float('inf'):
        return ""
    return s[sIndex: sIndex + int(minlen)]

# Minimum Window Subsequence
def minWindowII(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)

    min_len = float('inf')
    start_idx = -1

    s_idx = 0
    while s_idx < m:
        t_idx = 0

        while s_idx < m:
            if s1[s_idx] == s2[t_idx]:
                t_idx += 1
                if t_idx == n:
                    break
            s_idx += 1

        if t_idx < n:
            break

        end = s_idx
        t_idx = n - 1
        while s_idx >= 0:
            if s1[s_idx] == s2[t_idx]:
                t_idx -= 1
                if t_idx < 0:
                    break
            s_idx -= 1

        window_len = end - s_idx + 1
        if window_len < min_len:
            min_len = window_len
            start_idx = s_idx

        s_idx = s_idx + 1

    return '' if start_idx == -1 else s1[start_idx : start_idx + int(min_len)] 

# Number of substring containing all three Character
def numberOfSubstring(s: str) -> int:
    lstSeen = [-1] * 3
    cnt = 0

    for i in range(len(s)):
        lstSeen[ord(s[i]) - ord('a')] = i

        cnt += 1 + min(lstSeen[0], lstSeen[1], lstSeen[2])

    return cnt

# Count Number of Nice Subarray
def numberOfSubarrays(nums: list[int], k: int) -> int:
    left = 0
    cnt = 0
    res = 0
    prefix_evens = 0

    for r in range(len(nums)):
        if nums[r] & 1:
            cnt += 1
            prefix_evens = 0

        while cnt > k:
            if nums[left] & 1:
                cnt -= 1
            left += 1

        if cnt == k:
            while not (nums[left] & 1):
                prefix_evens += 1
                left += 1
            cnt -= 1
            left += 1
            prefix_evens += 1

        res += prefix_evens

    return res

# Binary Subarrays with sum
def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    def atmost(goal: int) -> int:
        if goal < 0:
            return 0

        summ = 0
        left = 0
        cnt = 0

        for r in range(len(nums)):
            summ += nums[r]

            while summ > goal:
                if nums[left] == 1:
                    summ -= 1
                left += 1

            cnt += r - left + 1

        return cnt
    return atmost(goal) - atmost(goal - 1)

# Subarray with K different Integers
def subarrayWithKDistinct(nums: list[int], k: int) -> int:
    def atmost(k):
        if k < 0:
            return 0

        left = 0
        d = {}
        cnt = 0

        for r in range(len(nums)):
            d[nums[r]] = d.get(nums[r], 0) + 1

            while len(d) > k:
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    del d[nums[left]]
                left += 1

            cnt += r - left + 1

        return cnt

    return atmost(k) - atmost(k - 1)

if __name__ == '__main__':
    print(subarrayWithKDistinct(nums = [1,2,1,2,3], k = 2))
