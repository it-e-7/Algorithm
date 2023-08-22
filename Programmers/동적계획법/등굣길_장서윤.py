def solution(m, n, puddles):
    # dp 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 물웅덩이 표시
    for m_, n_ in puddles:
        dp[n_][m_] = -1

    for n_ in range(1, n + 1):
        for m_ in range(1, m + 1):
            if n_ == 1 and m_ == 1:  # 시작점에 1을 넣어줌
                dp[n_][m_] = 1
                continue

            if dp[n_][m_] == -1:  # 물웅덩이를 만나면 0으로 바꿔줌
                dp[n_][m_] = 0
                continue

            # 현재 좌표의 좌측값과 상단의 값을 더해서 현재 dp의 값을 계산해줌
            dp[n_][m_] = dp[n_ - 1][m_] + dp[n_][m_ - 1]

    return dp[-1][-1] % 1000000007
