# Next Greater Element
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stk = []
    d = {}
    ans = []

    for i in range(len(nums2) - 1, -1, -1):
        if not stk:
            d[nums2[i]] = -1
        else:
            if stk[-1] > nums2[i]:
                d[nums2[i]] = stk[-1]
            else:
                while stk and stk[-1] < nums2[i]:
                    stk.pop()
                if stk:
                    d[nums2[i]] = stk[-1]
                else:
                    d[nums2[i]] = -1

        stk.append(nums2[i])

    for i in nums1:
        ans.append(d[i])

    return ans

# Next Greater Element II
def nextGreaterElementII(nums: list[int]) -> list[int]:
    stk = []
    n = len(nums)
    ans = [-1] * n

    for i in range(2 * (n - 1), -1, -1):
        while stk and stk[-1] <= nums[i % n]:
            stk.pop()

        if i < n:
            if stk:
                ans[i] = stk[-1]

        stk.append(nums[i % n])
    return ans

# Asteroid Collision
def asteroidCollision(asteroids: list[int]) -> list[int]:
    stk = []
    for a in asteroids:
        while stk and stk[-1] > 0 and a < 0:
            diff = a + stk[-1]
            if diff < 0:
                stk.pop()
            elif diff > 0:
                a = 0
            else:
                a = 0
                stk.pop()
        if a:
            stk.append(a)

    return stk

# Sum of Subarray Minimums (Not Optimised) -> Can use DP to optimise
def sumSubarrayMins(arr: list[int]) -> int:

    def _nextSmallerIndex(arr: list[int]) -> list[int]:
        ans = [-1] * len(arr)
        stk = []

        for i in range(len(arr) - 1, -1, -1):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            ans[i] = len(arr) if not stk else stk[-1]
            stk.append(i)

        return ans

    def _previousSmallerIndex(arr: list[int]) -> list[int]:
        ans = [-1] * len(arr)
        stk = []
        
        for i in range(len(arr)):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(i)
        
        return ans

    nsi = _nextSmallerIndex(arr)
    psi = _previousSmallerIndex(arr)
    mod = 1e9 + 7
    total = 0

    for i in range(len(arr)):
        left = i - psi[i]
        right = nsi[i] - i

        total += ((right * left * arr[i]) % mod) % mod

    return int(total)

# Sum of Subarray ranges
def subArrayRanges(arr: list[int]) -> int:
    def _nextSmallerIndex(arr: list[int]) -> list[int]:
        ans = [-1] * len(arr)
        stk = []
            
        for i in range(len(arr) - 1, -1, -1):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            ans[i] = len(arr) if not stk else stk[-1]
            stk.append(i)

        return ans

    def _previousSmallerIndex(arr: list[int]) -> list[int]:
        ans = [-1] * len(arr)
        stk = []
            
        for i in range(len(arr)):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(i)
            
        return ans

    def _previousLargestIndex(arr: list[int]) -> list[int]:
        ans = [-1] * len(arr)
        stk = []
            
        for i in range(len(arr)):
            while stk and arr[stk[-1]] < arr[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(i)
        
        return ans

    def _nextLargestIndex(arr: list[int]) -> list[int]:
        ans = [-1] * len(arr)
        stk = []
            
        for i in range(len(arr) - 1, -1, -1):
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop()
            ans[i] = len(arr) if not stk else stk[-1]
            stk.append(i)
            
        return ans

    nsi = _nextSmallerIndex(arr)
    psi = _previousSmallerIndex(arr)
    nli = _nextLargestIndex(arr)
    pli = _previousLargestIndex(arr)
    total_small = 0
    total_large = 0

    for i in range(len(arr)):
        left_small = i - psi[i]
        right_small = nsi[i] - i
        total_small += (right_small * left_small * arr[i])
            
        left_large = i - pli[i]
        right_large = nli[i] - i
        total_large += (right_large * left_large * arr[i])

    return total_large - total_small

# Remove K digits
def removekDigits(nums: str, k: int) -> str:
    if k == len(nums):
        return '0'

    stk = []
    ans = ''

    for i in nums:
        while stk and stk[-1] > i and k > 0:
            stk.pop()
            k -= 1
        stk.append(i)

    stk = stk[:len(stk) - k]

    while stk:
        ans += stk.pop()

    ans = ans.rstrip('0')
    if ans:
        return ans[::-1]
    return '0'

# Sliding Window Maximum
import collections

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    output = []
    q = collections.deque()

    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output

# Trapping Rain water
def trap(height):
    total = 0
    l = 0
    r = len(height) - 1
    leftMax = 0
    rightMax = 0

    while l < r:
        if height[l] <= height[r]:
            if leftMax > height[l]:
                total += leftMax - height[l]
            else:
                leftMax = height[l]
            l += 1 
        else:
            if rightMax > height[r]:
                total += rightMax - height[r]
            else:
                rightMax = height[r]
            r -= 1

    return total

if __name__ == '__main__':
    print(trap([4,2,0,3,2,5]))