from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    length = len(prices)
    while prices:
        selectNum = prices.popleft()
        count = 0
        length-=1
        if length==0:
            answer.append(0)
        else:
            for i in prices:
                if selectNum>i:
                    count+=1
                    break
                count+=1
            answer.append(count)
    
    return answer