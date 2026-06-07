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

if __name__ == '__main__':
    arr = [3,6,7,11]
    print(f'The minimum hours koko need to eat all bananas: {minEatingSpeed(arr, 8)}')