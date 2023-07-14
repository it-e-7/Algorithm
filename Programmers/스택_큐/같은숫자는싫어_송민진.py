from collections import deque
def solution(arr):
    q = deque(arr)
    answer = [q.popleft()]

    while q:
        checking = q.popleft()
        if answer and answer[-1] != checking:
            answer.append(checking)

    return answer