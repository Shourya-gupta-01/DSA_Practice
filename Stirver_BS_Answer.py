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

if __name__ == '__main__':
    x = 28
    print(f'The square root of {x} is {squreRoot(x)}')