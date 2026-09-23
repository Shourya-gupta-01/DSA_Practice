def checkIthBit(n: int, i: int) -> bool:
    return n & (1 << i) != 0

if __name__ == '__main__':
    print(checkIthBit(16, 3))
