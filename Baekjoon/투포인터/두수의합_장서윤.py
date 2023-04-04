n = int(input())
a = list()

a = list(map(int, input().split()))

x = int(input())

a.sort()

cnt = 0

start = 0
end = n-1

while start < end:
    if a[start] + a[end] > x:
        end -= 1
    elif a[start] + a[end] == x:
        cnt += 1
        end -= 1
    else:
        start+=1

print(cnt)

