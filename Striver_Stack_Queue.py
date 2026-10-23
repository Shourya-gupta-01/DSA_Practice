# Next Greater Element
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stk = []
    d = {}
    ans = []

    for i in range(len(nums2) - 1, -1, -1):
        if not stk:
            d[nums2[i]] = -1
        else:
            if stk[-1] > nums2[i]:
                d[nums2[i]] = stk[-1]
            else:
                while stk and stk[-1] < nums2[i]:
                    stk.pop()
                if stk:
                    d[nums2[i]] = stk[-1]
                else:
                    d[nums2[i]] = -1

        stk.append(nums2[i])

    for i in nums1:
        ans.append(d[i])

    return ans

if __name__ == '__main__':
    print(nextGreaterElement([4,1,2], [1,3,4,2]))