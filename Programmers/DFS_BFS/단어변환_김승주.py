from collections import deque

def solution(begin, target, words):
    
    if target not in words: # target이 없어서 변환할 수 없는 경우 
        return 0
    # 단어의 길이가 짧고 단어개수가 적으니 
    answer = 0
    visited = [ False for _ in range(len(words))]

    def bfs():
        q = deque()
        q.append((begin,0))
        
        while q:
            word, n_count = q.popleft()
            if word == target:
                return n_count
            else:
                for i in range(len(words)):
                    count =0
                    if not visited[i] :
                        for j in range(len(words[i])):
                            if words[i][j] != word[j]:
                                count+=1
                    if count ==1 :
                        visited[i] = True
                        q.append((words[i], n_count+1))
    answer= bfs()
        
    return answer