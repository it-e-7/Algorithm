import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
x = int(input().strip())

arr.sort()

answer = 0
left, right = 0, n-1
while left < right:
    now = arr[left] + arr[right]
    if now == x:
        answer += 1
        left += 1
    elif now < x:
        left += 1
    else:
        right -= 1

print(answer)
