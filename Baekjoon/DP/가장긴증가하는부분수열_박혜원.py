# [11053] 가장긴증가하는부분수열

N = int(input())
sequence = list(map(int, input().split()))

# dp테이블 생성 및 초기화)
dp = [1] * (N)

for i in range(1, N):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
