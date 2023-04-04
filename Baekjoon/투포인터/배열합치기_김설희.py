n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in sorted(A + B):
    print(i, end = ' ')