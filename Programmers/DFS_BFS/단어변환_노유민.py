from collections import deque


def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    q = deque()
    q.append((begin, 0))

    while q:
        word, count = q.popleft()
        if word == target:
            answer = count
            return answer
        else:
            for i in range(len(words)):
                tempCount = 0
                if visited[i] != True:
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            tempCount += 1

                    if tempCount == 1:
                        count += 1
                        q.append((words[i], count))
                        visited[i] = True

    return answer
