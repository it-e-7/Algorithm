def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:
                answer[i] = j - i
                break
        # 가격이 떨어지는 기간이 없을 때
        else:
            answer[i] = len(prices) - 1 - i

    return answer

'''
<출력결과>

i,j : (0, 1) => prices[j] , prices[i] : (2, 1)
i,j : (0, 2) => prices[j] , prices[i] : (3, 1)
i,j : (0, 3) => prices[j] , prices[i] : (2, 1)
i,j : (0, 4) => prices[j] , prices[i] : (3, 1)
-> else문
 
i,j : (1, 2) => prices[j] , prices[i] : (3, 2)
i,j : (1, 3) => prices[j] , prices[i] : (2, 2)
i,j : (1, 4) => prices[j] , prices[i] : (3, 2)
-> else문

i,j : (2, 3) => prices[j] , prices[i] : (2, 3)
-> answer[i] = j - i => 1

i,j : (3, 4) => prices[j] , prices[i] : (3, 2)
-> else문

'''