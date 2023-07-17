from collections import deque

def solution(prices):

    prices_queue = deque(prices)
    result = []
    while prices_queue:
        price = prices_queue.popleft()
        s = 0
        for p in prices_queue:
            s += 1
            if p < price:
                break
        result.append(s)

    return result