n, s = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
interval_sum = 0
cnt = 0
length = []

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += nums[end]
        end += 1
        cnt += 1

    if interval_sum >= s:
        length.append(cnt)

    cnt -= 1
    interval_sum -= nums[start]

if length:
    print(min(length))
else:
    print(0)