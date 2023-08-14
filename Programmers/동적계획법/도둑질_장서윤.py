def solution(money):
    answer = 0

    dp_f = [0 for _ in range(len(money))]
    dp_l = [0 for _ in range(len(money))]

    # 첫번째집 선택
    for i in range(len(money) - 1):
        if i == 0:
            dp_f[i] = money[i]
            continue
        if i == 1:
            dp_f[i] = max(dp_f[i - 1], money[i])
            continue

        # 앞의 두 집의 money에 따라 현재 집을 털지 말지 결정함
        # 인접한 집의 money가 더 큰 경우 현재 집을 털지 않음
        dp_f[i] = max(dp_f[i - 1], dp_f[i - 2] + money[i])

        # 첫번째집 선택 X
    for i in range(1, len(money)):
        if i == 1:
            dp_l[i] = money[i]
            continue

        dp_l[i] = max(dp_l[i - 1], dp_l[i - 2] + money[i])

    return max(dp_f[-2], dp_l[-1])