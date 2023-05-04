import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

dp=[1] *(n)


for i in range(0, len(numbers)): # 기준이 되는 애 
    for j in range(0, i) : # 바뀌면서 비교 되는 애 
        if numbers[j] < numbers[i] : # 기준이 되는 애가 크다면
            dp[i] = max(dp[j]+1 , dp[i])

print(max(dp))