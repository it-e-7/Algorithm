# [3273] 두 수의 합 (실버 3)
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
X = int(input())

A.sort()

left = 0
right = N-1
ans = 0

while left < right:
    tmp = A[left] + A[right]
    if tmp == X: ans += 1
    if tmp < X:
        left += 1
    else:
        right -= 1

print(ans)