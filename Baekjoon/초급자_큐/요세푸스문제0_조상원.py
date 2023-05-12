from collections import deque
n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])
ret = []
while q:
    q.rotate(-(k-1))
    # print(q)
    ret.append(q.popleft())
print("<{}>".format(", ".join(map(str, ret))))