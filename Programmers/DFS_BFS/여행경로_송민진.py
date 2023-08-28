def solution(tickets):
    global answer
    answer = []
    visited = [False] * len(tickets)

    dfs("ICN", ["ICN"], visited, tickets)
    answer.sort()
    return answer[0]


def dfs(dept, arr, visited, tickets):
    if len(arr) == len(tickets)+1:
        answer.append(arr)

    for i in range(len(tickets)):
        if tickets[i][0] == dept and not visited[i]:
            visited[i] = True
            dfs(tickets[i][1], arr+[tickets[i][1]], visited, tickets)
            visited[i] = False

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))