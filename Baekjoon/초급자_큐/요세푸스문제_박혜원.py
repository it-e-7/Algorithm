# [1158] 요세푸스 문제

import sys
from collections import deque

# 입력 받기
N, K = map(int, sys.stdin.readline().split())

queue = deque()
for i in range(1, N+1):
    queue.append(i)  # queue = [1,2,3,4,5,6,7]

answer = []

while len(queue) != 0:
    for _ in range(K-1):  # 인덱스가 0부터 시작하니까 k번째 -> K-1 번째
        # queue.popleft()로 첫 번째 요소를 제거하고, 이를 queue.append()
        queue.append(queue.popleft())
    answer.append(queue.popleft())


print("<", ", ".join(map(str, answer)), ">", sep="")
# sep="" 사용하는 이유 < 3, 6, 2, 7, 5, 1, 4 > ->  <3, 6, 2, 7, 5, 1, 4>
# ", ".join(map(str, answer) map은 정수를 문자형으로 바꾸고 콤마와 공백(", ")을 구분자로 사용하여 하나의 문자열로 결합한다.
