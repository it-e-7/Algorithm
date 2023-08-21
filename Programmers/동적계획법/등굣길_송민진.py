from collections import deque


def solution(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]
    board[0][0] = 1

    dx = [0, 1]
    dy = [1, 0]

    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if [ny + 1, nx + 1] in puddles:
                    continue
                board[nx][ny] += board[x][y]
                if (nx, ny) not in q:
                    q.append((nx, ny))
    return board[n - 1][m - 1] % 1000000007