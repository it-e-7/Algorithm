import sys
input = sys.stdin.readline

n = int(input())
# arr= [int(input()) for _ in range(n)]
# print(arr)
stack = []
result = []


cnt = 1

for i in range(n):
    # pass
    tmp = int(input())

    while cnt <= tmp:
        stack.append(cnt)
        result.append('+')
        cnt += 1
        print(f'stack : {stack} , result : {result}')

    if stack.pop() == tmp:

        result.append('-')
    else:
        print('NO')
        result.clear()
        break

for i in result:
    print(i)