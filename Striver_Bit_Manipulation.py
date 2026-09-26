# Check the Ith bit
from webbrowser import get
def checkIthBit(n: int, i: int) -> bool:
    return n & (1 << i) != 0

# Check if the number is odd
def checkOdd(n: int) -> bool:
    return n & 1 == 1

# Check if the number is power of 2 or not
def checkPower2(n: int) -> bool:
    return n & n - 1 == 0

# Count the number of set bits
def countSetBits(n: int) -> int:
    cnt = 0
    while n != 0:
        cnt += 1
        n = n & n - 1
    return cnt

# Swap two numbers
def swap(a: int, b: int) -> int:
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a, b)

# Minimum bit flips to convert number
def minBitFlips(start: int, goal: int) -> int:
    ans = start ^ goal
    cnt = 0
    while ans != 0:
        cnt += 1
        ans = ans & ans - 1
    return cnt

# Single Number-1
def singleNumber1(nums: list[int]) -> int:
    ans = 0
    for i in nums:
        ans ^= i
    return ans

# Single Number-2
# def singleNumber2(nums: list[int]) -> int: # Bit Solution Not Optimised
#     ans = 0
#     for bit_index in range(32):
#         cnt = 0
#         for i in range(len(nums)):
#             if nums[i] & 1 << bit_index:
#                 cnt += 1
#         if cnt % 3 != 0:
#             ans = ans | 1 << bit_index
#     return ans

def singleNumber2(nums: list[int]) -> int: #Bit solution Optimised
    ones, twos = 0, 0
    for i in range(len(nums)):
        ones = (ones ^ nums[i]) & ~twos
        twos = (twos ^ nums[i]) & ~ones
    return ones

# Single Number-3
def singleNumber3(nums: list[int]) -> list[int]:
    temp = 0
    for i in nums:
        temp ^= i

    rightMost = (temp & temp - 1) ^ temp

    b1, b2 = 0, 0

    for i in nums:
        if i & rightMost:
            b1 ^= i
        else:
            b2 ^= i
    return [b1, b2]

# Divide two number without multiplication and division
def divide(dividend: int, divisor: int) -> int:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    is_neg = (divisor < 0) ^ (dividend < 0)

    a, b = abs(dividend), abs(divisor)
    quotient = 0

    while a >= b:
        temp_divisor = b
        multiple = 1

        while a >= temp_divisor << 1:
            temp_divisor <<= 1
            multiple <<= 1

        a -= temp_divisor
        quotient += multiple

    if is_neg:
        quotient = -quotient

    return max(INT_MIN, min(INT_MAX, quotient))

# Power Set Bit Manipulation
def subsets(nums: list[int]) -> list[list[int]]:
    ans = []
    n_subset = 1 << len(nums)

    for i in range(n_subset):
        temp = []
        for j in range(len(nums)):
            if i & (1 << j):
                temp.append(nums[j])
        ans.append(temp)
    return ans

# XOR of elements in a given range
def findXOR(l: int, r: int) -> int:
    def getXOR(n):
        rem = n % 4
        if rem == 1:
            return 1
        elif rem == 2:
            return n + 1
        elif rem == 3:
            return 0
        return n

    xorL = getXOR(l - 1)
    xorR = getXOR(r)

    return xorR ^ xorL

if __name__ == '__main__':
    print(findXOR(4, 8))

