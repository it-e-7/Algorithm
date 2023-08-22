def solution(money):
    #첫번째 집과 마지막 집이 인접해있음
    #첫번쨰를 무조건 터는 경우와 마지막 집을 무조건 터는 경우로 계산
    first_house = [0] * len(money)
    first_house[0] = money[0]
    first_house[1] = max(money[0], money[1])

    for i in range(2, len(money)-1):
        first_house[i] = max(first_house[i-1], money[i]+first_house[i-2])

    last_house = [0] * len(money)
    last_house[0] = 0
    last_house[1] = money[1]

    for i in range(2, len(money)):
        last_house[i] = max(last_house[i-1], money[i]+last_house[i-2])

    return max(max(first_house), max(last_house))
