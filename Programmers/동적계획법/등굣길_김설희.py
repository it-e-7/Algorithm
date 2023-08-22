
# m, n이 1이상 100 이하, 물에 잠긴 지역은 0 이상 100 이하
# 최단경로 개수 문제
# dfs - 시간 초과, 재귀라서 2^(m+n)의 시간 복잡도라고.. => DP 이용
'''
def solution(m, n, puddles):
    region = [[0] * n for _ in range(m)]
    if puddles:
        for p in puddles:
            region[p[0] - 1][p[1] - 1] = 2 # 주의주의

    dx = [1, 0]
    dy = [0, 1]

    cnt = 0

    def dfs(x, y):
        nonlocal cnt
        if x == m - 1 and y == n - 1:
            cnt += 1
        else:
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and region[nx][ny] == 0:
                    region[nx][ny] = 1
                    dfs(nx, ny)
                    region[nx][ny] = 0

    region[0][0] = 1
    dfs(0, 0)

    return cnt % 1000000007
'''

def solution(m, n, puddles):
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for x, y in puddles:
        dp[x - 1][y - 1] = -1

    for x in range(m):
        for y in range(n):
            if dp[x][y] == -1:
                continue # 기억행

            if x - 1 >= 0 and dp[x - 1][y] != -1:
                dp[x][y] += dp[x - 1][y]

            if y - 1 >= 0 and dp[x][y - 1] != -1:
                dp[x][y] += dp[x][y - 1]

    for i in dp:
        print(i)

    return dp[m - 1][n - 1] % 1000000007

print(solution(4, 3, [[2, 2]]))