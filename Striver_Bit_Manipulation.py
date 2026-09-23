def checkIthBit(n: int, i: int) -> bool:
    return n & (1 << i) != 0

def checkOdd(n: int) -> bool:
    return n & 1 == 1

if __name__ == '__main__':
    print(checkOdd(13))
