# Assign Cookies
def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()

    l, r = 0, 0
    cnt = 0

    while l < len(g) and r < len(s):
        if g[l] <= s[r]:
            l += 1
            cnt += 1
        r += 1
    
    return cnt

# Lemonade Change
def lemonadeChange(bills: list[int]) -> bool:
    galla5 = 0
    galla10 = 0

    for i in bills:
        if i == 5:
            galla5 += 1
        elif i == galla10:
            if galla5:
                galla5 -= 1
                galla10 += 1
            else:
                return False
        elif i == 20:
            if galla5 and galla10:
                galla5 -= 1
                galla10 -= 1
            elif galla5 >= 3:
                galla5 -= 3
            else:
                return False
    return True

if __name__ == '__main__':
    print(lemonadeChange([5,5,10,10,20]))
