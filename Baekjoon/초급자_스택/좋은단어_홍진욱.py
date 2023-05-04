import string
import sys

result =0
n = int(input())

for i in range(n):
    stack = []
    temp = 0

    s = sys.stdin.readline().strip()
    for j in range(len(s)):
        if len(stack) == 0 or s[j] != stack[-1]:
            stack.append(s[j])
        else:
            stack.pop()
            temp += 1
    if len(stack) == 0:
        result += 1

print(result)
