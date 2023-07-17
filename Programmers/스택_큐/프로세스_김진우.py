'''from collections import deque

def solution(priorities, location):
    answer = 0
    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0

answer = []
cnt = 0
while priorities:
    max_num = max(priorities)

    if priorities[0] == max_num:
        print(max_num)
        priorities.pop(0)
        if len(priorities) == 0 :
            break
        max_num = max(priorities)
        print(f'if문의 {cnt}')
        answer.append(cnt)
        cnt = 0
        cnt += 1
    else:
        priorities.append(priorities[0])
        print(priorities)
        priorities.pop(0)
        cnt += 1
        print(f'cnt : {cnt}')
print(f'answer : {answer}')
print(answer[location])'''

######################################
'''from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])  # (인덱스, 우선순위) 쌍으로 큐에 저장
    while queue:
        task = queue.popleft()
        if any(task[1] < q[1] for q in queue):  # 우선순위가 더 높은 작업이 있다면 큐의 맨 뒤로 보냄
            queue.append(task)
        else:
            answer += 1  # 우선순위가 가장 높은 작업이면 처리하고 순서를 증가시킴
            if task[0] == location:
                return answer
'''
#####################################
'''def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            priorities.pop(0)
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
'''

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
