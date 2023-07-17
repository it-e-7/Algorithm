from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([])
    for i in range(len(priorities)):
        if i == location:
            q.append((priorities[i], True))
        else:
            q.append((priorities[i], False))

    priorities.sort()

    while q:
        now = q.popleft()
        if now[0] == priorities[-1]:
            priorities.pop()
            answer += 1
            if now[1]:
                break
        else:
            q.append(now)

    return answer