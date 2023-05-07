arr = list(input())

s = []
c = 0

for i, v in enumerate(arr):
    if v == '(':
        s.append(v)
    else:
        if arr[i-1] == '(':
            s.pop()
            c += len(s)
        else:
            s.pop()
            c += 1

print(c)
