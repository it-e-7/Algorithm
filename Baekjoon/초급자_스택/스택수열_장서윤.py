import sys

n = int(sys.stdin.readline())

stack = []
ans = []
cnt = 0

b = True

for i in range(n):
    num = int(sys.stdin.readline())
    while cnt < num:
        cnt += 1
        ans.append("+")
        stack.append(cnt)

    if num == stack[-1]:
        stack.pop()
        ans.append("-")
    else:
        b = False

if b:
    for v in ans:
        print(v)

else:
    print("NO")