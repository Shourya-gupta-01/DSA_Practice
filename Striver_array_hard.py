# Pascal's Triangle
def pascalTriangle(numRows):
    dummy = [[1]]
    res = []
    flag = True
    cnt = 1

    if numRows == 1:
        return dummy
        
    while flag:
        res = [1]
        for i in range(len(dummy[-1]) - 1):
            res.append(dummy[-1][i] + dummy[-1][i + 1])

        res.append(1)
        dummy.append(res)
        res = []
        cnt += 1

        if cnt == numRows:
            flag = False

    return dummy

# Majority Element 2 --> Boyer Moore Algorithim
def majorityElement(nums):
    count1 = count2 = 0
    cand1 = cand2 = None
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    return [n for n in (cand1, cand2) if nums.count(n) > len(nums) // 3]

# 3Sum
def threeSum(nums):
    ans = []
    nums.sort()
    for k in range(len(nums)):
        if k>0 and nums[k]==nums[k-1]:
            continue
        i=k+1
        j=len(nums)-1
        while i<j:
            summ=nums[k]+nums[i]+nums[j]
            if summ==0:
                ans.append(sorted([nums[i], nums[j], nums[k]]))
                i+=1
                while nums[i]==nums[i-1] and i<j:
                    i+=1
            elif summ>0:
                j-=1
            else:
                i+=1
    return ans

# 4Sum
def fourSum(arr, target):
    n = len(arr)
    arr.sort()
    ans = []

    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = arr[i] + arr[j] + arr[left] + arr[right]
                if total == target:
                    ans.append([arr[i], arr[j], arr[left], arr[right]])
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return ans

# Largest Subarray with sum 0
def zeroSubarray(arr):
    d = {}
    cum_sum = 0
    ans = 0

    for i in range(len(arr)):
        if cum_sum not in d:
            d[cum_sum] = i
        cum_sum += arr[i]

        if cum_sum in d:
            ans = max(ans, i - d[cum_sum] + 1)

    return ans

# Count the number of subarray with given XOR k
def countSubarraysXOR(arr, k):
    d = {0:1}
    xr = 0
    res = 0
    for i in arr:
        xr ^= i
        if xr ^ k in d:
            res += d[xr ^ k]
        if xr not in d:
            d[xr] = 1
        else:
            d[xr] += 1
    return res

# Merge overlapping sub-intervals
def mergeIntervals(intervals):
    intervals.sort(key = lambda interval: interval[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = interval[1]

    return merged

# Merge two sorted arrays without extra space
def mergeArrays(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

# Find the repeating and missing number (Better Approach)
def findMissingRepeatingNumbers(arr):
    n = len(arr)
    ans = []
    d = {}
    summ = 0
    for i in arr:
        if i in d:
            d[i] += 1
            if d[i] == 2:
                ans.append(i)        
        else:
            d[i] = 1
        summ += i

    missing = (n * ((n + 1) / 2)) - (summ - ans[0])
    ans.append(missing)

    return ans

# Find the repeating and missing number (Optimal Approach 1) Space Complexity --> O(1)
def findMissingRepeatingNumbers(nums):
    n = len(nums)
    SN = (n * (n + 1)) // 2

    S2N = (n * (n + 1) * (2 * n + 1)) // 6

    S = 0
    S2 = 0
    for num in nums:
        S += num
        S2 += num * num

    val1 = S - SN

    val2 = S2 - S2N

    # Calculate X + Y using X + Y = (X^2 - Y^2) / (X - Y)
    val2 = val2 // val1

    x = (val1 + val2) // 2
    y = x - val1

    # Return the results as [repeating, missing]
    return [int(x), int(y)]

# Find the repeating and missing number (Optimal Approach 2) Space Complexity --> O(1)
def findMissingRepeatingNumbers(nums):
    pass

# Count Inversions in an array
def numberOfInversions(arr):
    ans = 0
    def merge_sort(arr, low, high):
        if low == high:
            return
        mid = low + (high - low) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

    def merge(arr, low, mid, high):
        nonlocal ans
        temp = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                ans += mid - left + 1
                right += 1

        if left <= mid:
            temp.extend(arr[left:mid + 1])

        if right <= high:
            temp.extend(arr[right:high + 1])

        for i in range(len(temp)):
            arr[low + i] = temp[i]

    merge_sort(arr, 0, len(arr) - 1)
    return ans

# Reverse Pairs
def reversePairs(arr):
    ans = 0
    def merge_sort(arr, low, high):
        if low == high:
            return
        mid = low + (high - low) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

    def merge(arr, low, mid, high):
        nonlocal ans
        temp = []
        left = low
        right = mid + 1

        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            ans += (right - (mid + 1))

        right = mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        if left <= mid:
            temp.extend(arr[left:mid + 1])

        if right <= high:
            temp.extend(arr[right:high + 1])

        for i in range(len(temp)):
            arr[low + i] = temp[i]

    merge_sort(arr, 0, len(arr) - 1)
    return ans

# Maximum Product Subarray
def maxProductSubarray(arr):
    curMax, curMin = 1, 1
    res = max(arr)
    for n in arr:
        if n == 0:
            curMax, curMin = 1, 1
            continue
        curMax = max(curMax * n, curMin * n, n)
        curMin = min(curMax * n, curMin * n, n)
        res = max(res, curMax)
    return res

if __name__ == "__main__":
    arr = [2,4,0,5,1, 6]
    # print(f'The Pascal Triangle {pascalTriangle(4)}')
    # ans = majorityElement(arr)
    # print("The majority elements are:", ans)
    # print(f'The target sum is of : {fourSum(arr, 0)}')
    # print(f'Longest subarray with sum 0 : {zeroSubarray(arr)}')
    # print(f'The Number of Subarray with XOR k : {countSubarraysXOR(arr, 6)}')
    # print(f'The merged intervals are : {mergeIntervals(arr)}')
    # mergeArrays(arr1 ,3 ,arr2, 3)
    # print(f'The merged arrays are : {arr1}')
    # print(f'The repeating and missing numbers are : {findMissingRepeatingNumbers(arr)}')
    # print(f'The Number of Inversion in the given array are : {numberOfInversions(arr)}')
    # print(f'The Number of Reverse Pairs in the given array are : {reversePairs(arr)}')
    print(f'The Maximum Product Subarray in an array is : {maxProductSubarray(arr)}')