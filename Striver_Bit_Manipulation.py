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


if __name__ == '__main__':
    a = 10
    b = 20
    a, b = swap(a, b)
    print(a, b)
