n, k = map(int, input().split())
arr = list(range(1, n+1))
result = []

while arr:
    n = (n + k - 1) % len(arr)
    result.append(arr.pop(n))
print('<' + ', '.join(map(str, result)) + '>')

