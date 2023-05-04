import sys

input = sys.stdin.readline

n = int(input())

arr = [input().strip() for _ in range(n)]

c = 0
for w in arr:
    s = []

    for i, v in enumerate(w):
        if not s:
            s.append(v)
        else:
            if v == s[-1]:
                s.pop()
            else:
                s.append(v)

    if not s:
        c += 1

print(c)
