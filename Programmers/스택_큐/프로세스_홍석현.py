from collections import deque


def solution(priorities, location):
    answer = 0
    stack = deque()

    for i in range(len(priorities)):
        stack.append([i, priorities[i]])

    priorities.sort()

    while stack:
        i, p = stack.popleft()

        if p < priorities[-1]:
            stack.append([i, p])
        elif p == priorities[-1]:
            answer += 1
            priorities.pop()

            if i == location:
                break
    return answer


###################################################################
def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer