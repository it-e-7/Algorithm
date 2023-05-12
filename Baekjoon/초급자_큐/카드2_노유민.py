import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

q=deque()

for i in range(n):
    q.append(i+1)

i=1
while(len(q)>1):
    if i%2!=0:
        q.popleft()
        i+=1
    else:
        idx=q.popleft()
        q.append(idx)
        i+=1

print(q[0])

