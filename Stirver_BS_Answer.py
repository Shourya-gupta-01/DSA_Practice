# Square root of a number
def squreRoot(x: int) -> int:
    if x < 2:
        return x
    left = 1
    right = x // 2
    ans = 0
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

# Nth root of a number
def nroot(x: int, y: int) -> int:
    left = 1
    right = y

    while left <= right:
        mid = left + (right - left) // 2
        if mid ** x == y:
            return mid
        elif mid ** x < y:
            left = mid + 1
        else:
            right = mid - 1
    return mid

# Koko eating bananas
def minEatingSpeed(piles: list[int], h: int) -> int:
    def helper(piles: list[int], k: int) -> int:
        time = 0
        for i in piles:
            time += (i // k) + 1
        return time

    ans = float('inf')
    left = 0
    right = max(piles)
    while left <= right:
        mid = left + (right - left) // 2
        if helper(piles, mid) <= h:
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1
    return ans

# Minimum days to make m bouquets
def minDays(bloomDay, m, k):
    def ispossible(bloomDay, m, k, dtb):
        cnt = 0
        b = 0
        for i in bloomDay:
            if i <= dtb:
                cnt += 1
                if cnt == k:
                    b += 1
                    cnt = 0
                if m == b:
                    return True
            else:
                cnt = 0
        return b >= m
    
    if m * k > len(bloomDay):
        return -1
    left = 0
    right = max(bloomDay) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if ispossible(bloomDay, m, k, mid):
            right = mid -1
        else:
            left = mid + 1
    return left

# Find the smallest divisor given a threshold
def smallestDivisor(nums, threshold):
    def compute(nums, divisor):
        summ = 0
        for i in nums:
            # Important formula to calculate ceil value
            summ += -(-i//divisor)
        return summ
                
    left = 1
    right = max(nums)

    while left <= right:
        mid = left + (right - left) // 2
        if compute(nums, mid) > threshold:
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == '__main__':
    arr = [1,2,5,9]
    print(f'The Smallest divisor is {smallestDivisor(arr, 6)}')