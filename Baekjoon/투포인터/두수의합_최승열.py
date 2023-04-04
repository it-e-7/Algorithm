# [3273] 두 수의 합
# https://www.acmicpc.net/problem/3273

N = int(input().strip())
num = list(map(int, input().strip().split()))
X = int(input().strip())

S = {}
ans = 0
for n in num:
    if X-n in S:
        ans += 1
    S[n]=None
print(ans)