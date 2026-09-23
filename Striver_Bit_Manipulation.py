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

if __name__ == '__main__':
    print(countSetBits(11))
