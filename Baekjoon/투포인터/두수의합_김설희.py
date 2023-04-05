n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

start, end = 0, n-1
cnt = 0

while start < end:
    if nums[start] + nums[end] == x:
        start += 1
        cnt += 1
    elif nums[start] + nums[end] > x:
        end -= 1
    else:
        start += 1

print(cnt)
