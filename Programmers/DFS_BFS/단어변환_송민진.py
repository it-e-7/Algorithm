from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    words.append(begin)
    words_dict = {word: [] for word in words}

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            cnt = 0
            for idx in range(len(words[i])):
                if words[i][idx] != words[j][idx]:
                    cnt += 1
            if cnt == 1:
                words_dict[words[i]].append(words[j])
                words_dict[words[j]].append(words[i])


    q = deque([(begin, 0)])
    visited = []
    while q:
        now, cnt = q.popleft()
        if target in words_dict[now]:
            return cnt + 1
        elif words_dict[now]:
            for w in words_dict[now]:
                if w not in visited:
                    q.append((w, cnt + 1))
                    visited.append(w)
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution("aab", "aba", ["abb", "aba"]))