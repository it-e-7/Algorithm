import sys

n = int(input())

arr = [list(sys.stdin.readline().split()) for _ in range(n)]

reversed_arr = []
for i in range(n):
    reversed_arr.append(' '.join(reversed(arr[i])))


for i in range(n):
    print("Case #"+str(i+1)+": "+reversed_arr[i])
