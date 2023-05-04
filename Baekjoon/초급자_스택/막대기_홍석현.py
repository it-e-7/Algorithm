N = int(input())


arr = [int(input()) for _ in range(N)][::-1]

stack = [arr[0]]
for i in range(1, N):
    if arr[i] > stack[-1]:
        stack.append(arr[i])

print(len(stack))