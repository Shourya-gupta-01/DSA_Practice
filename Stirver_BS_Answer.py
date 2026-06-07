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

if __name__ == '__main__':
    x = 27
    print(f'The nth root of {x} is {nroot(3, 125)}')