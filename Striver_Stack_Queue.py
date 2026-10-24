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

    def _previousLargestIndex(arr):
        ans = [-1] * len(arr)
        stk = []
            
        for i in range(len(arr)):
            while stk and arr[stk[-1]] < arr[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(i)
        
        return ans

    def _nextLargestIndex(arr):
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

if __name__ == '__main__':
    print(subArrayRanges([-20592,-83117,16783,-75446,-27276,84170,-31295,60725,40504,55534,69043,-66679,-37739,59243,33435,-54421,-28323,52328,88286,-8950,-83012,-56787,33721,32043,-82896,-14383,-83955,16283,-61726,-42147,61811,-85513,31713,-1515,73524,18560,83506,-52750,55842,-5015,16664,-61757,44559,-76619,-10654,-68067,-66325,-11056,-27075,-57573,-40458,-20842,-97777,66133,-37575,31086,75837,-41855,-25531,56400,-33690,-39164,66261,-21294,-12404,-33518,93478,71963,-11822,90390,-52285,21353,-84139,-29364,64014,-34432,-82059,-73154,-42019,-15953,-22827,-43816,-40779,-28328,-98246,85909,87644,-44864,-85428,-57242,-82063,33286,68152,-38673,69128,-156,63600,-1288,15353,88223,65697,15022,-43178,89189,49340,-78699,-42045,66750,-55751,16339,31898,-26805,-52744,41579,-51245,-50475,63095,74967,19004,-8199,-76578,-90525,-79107,-48494,131,-33587,23005,89521,-72712,1210,-95145,53575,-49158,-13969,10358,-21825,78978,70410,15822,-79109,39030,-26834,-935,-61020,-86144,59761,-83719,-34522,37703,-43117,39510,49971,82129,7888,13840,-68891,-4570,25392,36337,-61182,61456,46340,32956,-30114,85336,37163,88134,-13770,39635,76952,22120,-31433,31457,70979,11894,47119,-58116,-77836,-19079,-29708,17538,-18605,86884,64608,-49294,-15356,85231,20870,-23490,70947,76657,50403,28211,122,34434,-55828,-82124,39606,73883,22631,-55381,-49969,15555,-34013,-29094,20189,-87109,63481,2203,69698,-86994,-43637,-77345,-40796]))