def solution(triangle):
    N = len(triangle)
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = triangle[0][0]

    for i in range(0, N - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    return max(dp[-1])