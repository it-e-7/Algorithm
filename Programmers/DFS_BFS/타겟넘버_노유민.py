def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])  # 그 다음값을 더하고 빼고
            dfs(idx+1, result-numbers[idx])
    dfs(0, 0)
    return answer
