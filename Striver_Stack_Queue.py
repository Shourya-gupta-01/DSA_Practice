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

if __name__ == '__main__':
    print(sumSubarrayMins([11,81,94,43,3]))