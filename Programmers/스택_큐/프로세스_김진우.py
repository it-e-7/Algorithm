from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))

    while True:
        task = queue.popleft()
        if any(task[1] < q[1] for q in queue):
            queue.append(task)
        else:
            answer += 1
            if task[0] == location:
                break

    return answer
