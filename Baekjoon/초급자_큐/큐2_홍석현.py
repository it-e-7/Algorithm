import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] =='front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] =='back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif command[0] =='size':
        print(len(q))
    elif command[0] =='empty':
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == 'pop':
        if q:
            ppop = q.popleft()
            print(ppop)
        else:
            print(-1)
