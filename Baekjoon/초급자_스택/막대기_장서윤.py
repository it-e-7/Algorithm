import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    stack.append(int(sys.stdin.readline()))

long = stack.pop()
cnt = 1
for i in range(len(stack)-1, -1, -1):
    if long < stack[i]:
        long = stack[i]
        cnt +=1

print(cnt)