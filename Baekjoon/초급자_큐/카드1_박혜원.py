# [2161] 카드1
import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
answer = []
for i in range(1, n+1):
    queue.append(i)  # [1,2,3,4,5,6,7]

while len(queue) != 0:
    answer.append(queue.popleft())
    if len(queue) != 0:
        queue.append(queue.popleft())


print(*answer)
