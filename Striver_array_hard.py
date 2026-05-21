# Pascal's Triangle
def pascalTriangle(numRows):
    dummy = [[1]]
    res = []
    flag = True
    cnt = 1

    if numRows == 1:
        return dummy
        
    while flag:
        res = [1]
        for i in range(len(dummy[-1]) - 1):
            res.append(dummy[-1][i] + dummy[-1][i + 1])

        res.append(1)
        dummy.append(res)
        res = []
        cnt += 1

        if cnt == numRows:
            flag = False

    return dummy

# Majority Element 2 --> Boyer Moore Algorithim
def majorityElement(nums):
    count1 = count2 = 0
    cand1 = cand2 = None
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    return [n for n in (cand1, cand2) if nums.count(n) > len(nums) // 3]

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    # print(f'The Pascal Triangle {pascalTriangle(4)}')
    ans = majorityElement(arr)
    print("The majority elements are:", ans)