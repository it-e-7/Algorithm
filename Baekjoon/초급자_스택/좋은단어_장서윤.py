import sys

n = int(input())

cnt = 0
for i in range(n):
    stack = []
    word = sys.stdin.readline().strip()

    for j in range(len(word)):
        if len(stack) > 0 and word[j] == stack[-1]:
            stack.pop()
        else:
            stack.append(word[j])
    if len(stack) == 0:
        cnt += 1
print(cnt)
