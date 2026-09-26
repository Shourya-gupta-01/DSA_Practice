# Check the Ith bit
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
    return a, b

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

if __name__ == '__main__':
    print(singleNumber2([2,2,2,5,5,5,3]))

