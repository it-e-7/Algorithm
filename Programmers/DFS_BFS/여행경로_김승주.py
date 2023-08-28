def solution(tickets):
    answer = []
    
    visited = [False] * len(tickets)

    # dfs로
    def dfs(start_point, root):
        
        if len(tickets) +1 == len(root):
            answer.append(root)
            return 
        for idx, ticket in enumerate(tickets):
            if start_point == ticket[0] and not visited[idx] :
                visited[idx] = True
                dfs(ticket[1], root+[ticket[1]])
                visited[idx]  = False # 백트래킹
    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]