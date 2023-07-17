def solution(prices):
    answer = []

    for f in range(len(prices)):
        tmp = 0
        for s in range(f, len(prices)):
            tmp+=1
            if prices[f] > prices[s]:
                break
        answer.append(tmp-1)

    return answer
