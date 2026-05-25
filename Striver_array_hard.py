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

# 3Sum
def threeSum(nums):
    ans = []
    nums.sort()
    for k in range(len(nums)):
        if k>0 and nums[k]==nums[k-1]:
            continue
        i=k+1
        j=len(nums)-1
        while i<j:
            summ=nums[k]+nums[i]+nums[j]
            if summ==0:
                ans.append(sorted([nums[i], nums[j], nums[k]]))
                i+=1
                while nums[i]==nums[i-1] and i<j:
                    i+=1
            elif summ>0:
                j-=1
            else:
                i+=1
    return ans

# 4Sum
def fourSum(arr, target):
    n = len(arr)
    arr.sort()
    ans = []

    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = arr[i] + arr[j] + arr[left] + arr[right]
                if total == target:
                    ans.append([arr[i], arr[j], arr[left], arr[right]])
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return ans

if __name__ == "__main__":
    arr = [1,0,-1,0,-2,2]
    # print(f'The Pascal Triangle {pascalTriangle(4)}')
    # ans = majorityElement(arr)
    # print("The majority elements are:", ans)
    print(f'The target sum is of : {fourSum(arr, 0)}')