def solution(triangle):
    # dp 초기화
    dp = [[0] * (len(triangle)) for _ in range(len(triangle))]

    # bottom-up 방식
    for i in range(len(triangle) - 1, -1, -1):
        for j in range(len(triangle[i])):
            # 마지막 행인 경우 dp에 triangle 값을 그대로 넣어줌
            if i == len(triangle) - 1:
                dp[i][j] = triangle[i][j]
                continue
            # 왼쪽 대각선 값과 오른쪽 대각선 값을 비교해서 더 큰 값을 더해준 뒤 dp 에 저장
            dp[i][j] = triangle[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])

    # dp 최상단 값을 return 함
    return dp[0][0]