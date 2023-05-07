import sys

input = sys.stdin.readline

n = int(input())

arrs = [input().split() for _ in range(n)]

# print(arrs)
for i, arr in enumerate(arrs):
    rev = ' '.join(arr[::-1])
    idx = i+1
    print(f"Case #{idx}: {rev}")