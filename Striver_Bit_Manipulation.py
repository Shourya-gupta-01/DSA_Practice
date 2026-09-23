# Check the Ith bit
def checkIthBit(n: int, i: int) -> bool:
    return n & (1 << i) != 0

# Check if the number is odd
def checkOdd(n: int) -> bool:
    return n & 1 == 1

# Check if the number is power of 2 or not
def checkPower2(n: int) -> bool:
    return n & n - 1 == 0

if __name__ == '__main__':
    print(checkPower2(8))
