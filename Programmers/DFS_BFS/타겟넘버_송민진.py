def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, 0, target)
    return answer

def dfs(depth, numbers, tmp, target):
    global answer

    if depth == len(numbers):
        if tmp == target:
            answer += 1
        return

    dfs(depth+1, numbers, tmp+numbers[depth], target)
    dfs(depth+1, numbers, tmp-numbers[depth], target)