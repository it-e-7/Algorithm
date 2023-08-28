from collections import deque
# 테케 1,2번 실패
# def solution(tickets):
#     answer = []
#     q=deque()
#     tickets.sort(key=lambda x:x[1])
#     visited=[False for _ in range(len(tickets))]
#     for i in range(len(tickets)):
#         if tickets[i][0]=='ICN':
#             q.append((tickets[i][0],tickets[i][1]))
#             visited[i]=True
#             break

#     while q:
#         start,end =q.popleft()
#         answer.append(start)
#         for i in range(len(tickets)):
#             if tickets[i][0]==end and visited[i]==False:
#                 q.append((tickets[i][0],tickets[i][1]))
#                 visited[i]=True
#                 break

#     answer.append(end)
#     return answer


def solution(tickets):
    answer = []
    graph = {}

    for start, end in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]

    for key in graph.keys():
        graph[key].sort(reverse=True)

    q = deque(["ICN"])

    while q:
        current = q[-1]
        if current in graph and graph[current]:
            q.append(graph[current].pop())
        else:
            # popleft해서 그냥 담는게 안되는 예시 [["ICN","A"],["ICN","B"],["B","ICN"]]
            answer.append(q.pop())
    answer.reverse()
    return answer
