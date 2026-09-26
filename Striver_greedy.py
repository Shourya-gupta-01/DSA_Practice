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

# Fractional Knapsack
def fractionalKnapsack(val: list[int], wt: list[int], capacity: int) -> int:
    items = []
    profit = 0
    for i in range(len(val)):
        items.append([val[i] / wt[i], val[i], wt[i]])

    items.sort(key = lambda x: x[0])

    while items and capacity >= items[-1][2]:
        profit += items[-1][1]
        capacity -= items[-1][2]
        items.pop()

    if items and capacity > 0:
        profit += (capacity / items[-1][2]) * items[-1][1]

    return profit

if __name__ == '__main__':
    print(fractionalKnapsack([60, 100, 120], [10, 20, 30], 50))
