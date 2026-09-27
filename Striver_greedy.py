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
def fractionalKnapsack(val: list[int], wt: list[int], capacity: float) -> float:
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

# Jump Game-1
def canJump(nums: list[int]) -> bool:
    maxIndex = 0
    for i in range(len(nums)):
        if i <= maxIndex:
            maxIndex = max(maxIndex, nums[i] + i)
        else:
            return False
    return True

# Shortest Job First
def sjf(bt: list[int]) -> int:
    bt.sort()
    wt = [0]

    for i in bt:
        wt.append(wt[-1] + i)

    return sum(wt[:-1]) // len(bt)

# Job Sequencing Problem (Not Optimized)
def jobSequencing(deadline: list[int], profit: list[int]) -> list[int]:
    jobs = sorted(zip(deadline, profit), key = lambda x: x[1], reverse = True)

    max_deadline = max(deadline) if deadline else 0
    slots = [-1] * (max_deadline + 1)

    cnt_jobs = 0
    max_profit = 0

    for d, p in jobs:
        for slot in range(d, 0, -1):
            if slots[slot] == -1:
                slots[slot] = 1
                cnt_jobs += 1
                max_profit += p
                break

    return [cnt_jobs, max_profit]


# N meetings in a room
def maxMeetings(start: list[int], end: list[int]) -> list[int]:
    ans = []
    meetings = []
    for i in range(len(start)):
        meetings.append((start[i], end[i], i))

    meetings.sort(key = lambda x: (x[1], x[2]))
    endtime = -1

    for i in meetings:
        if endtime < i[0]:
            ans.append(i[2] + 1)
            endtime = i[1]
    return sorted(ans)

if __name__ == '__main__':
    print(maxMeetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
