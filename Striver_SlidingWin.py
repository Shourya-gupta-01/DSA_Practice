# Maximum points you can obtain from cards 
def maxScore(cardPoints: list[int], k: int) -> int:
    ans = sum(cardPoints[:k])
    curr_sum = ans
    temp = k
    cnt = 0

    while cnt < k:
        cnt += 1
        curr_sum += cardPoints[len(cardPoints) - cnt]
        curr_sum -= cardPoints[temp - 1]
        temp -= 1
        ans = max(curr_sum, ans)
        
    return ans

if __name__ == '__main__':
    print(maxScore([1,2,3,4,5,6,1], 3))


