import sys

n = int(sys.stdin.readline().rstrip())

ans = 0
row = [0] * n


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def dfs(x):
    global ans
    if x == n:
        ans += 1

    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)


dfs(0)
print(ans)