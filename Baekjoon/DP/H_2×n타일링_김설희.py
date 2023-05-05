n = int(input())
dp = [0] * 1001
# n이 홀수일 때와 짝수일 때로 나뉜다는 것!

dp[1] = 1
dp[2] = 2 # 첫번째 홀수인 1과 짝수인 2의 경우
for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)