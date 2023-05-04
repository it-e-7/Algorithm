import sys
input = sys.stdin.readline

k = int(input())

arr = []

for _ in range(k):
    i = int(input())
    if i == 0 and len(arr) == 0 :
        continue
    elif i == 0 and len(arr) != 0:
        arr.pop()
    else:
        arr.append(i)
        # pop()안에 아무것도 넣지않으면 마지막 인덱스가 지워진다

print(sum(arr))