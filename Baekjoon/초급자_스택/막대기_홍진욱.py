import sys

n = int(input())
stack =[]
max =0
result=0
for i in range(n):
    stack.append(int(sys.stdin.readline().strip()))

for i in range(n):
    num = stack.pop()
    if num > max:
        max = num
        result += 1

print(result)
