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

if __name__ == '__main__':
    print(findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
