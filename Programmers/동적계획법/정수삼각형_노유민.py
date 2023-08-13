def solution(triangle):
    answer = 0
    dp = []
    dp.append([triangle[0][0]])  # 초기화

    for i in range(1, len(triangle)):
        dp_row = []  # 현재 리스트
        for j in range(len(triangle[i])):
            if j == 0:
                dp_row.append(dp[i - 1][j] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                dp_row.append(dp[i - 1][j - 1] + triangle[i][j])
            else:
                dp_row.append(
                    max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j])
        dp.append(dp_row)  # dp에 추가

    # max값 찾기
    answer = max(dp[-1])

    return answer
