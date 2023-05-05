import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

end = arr.pop()
c = 1
while arr:
    n = arr.pop()
    if n > end:
        end = n
        c+=1

print(c)